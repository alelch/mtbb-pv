// supabase/functions/pv-lead/index.ts
// Recebe leads das páginas MTBB-PV (pré-checkout / lista de espera)
// e sincroniza com ActiveCampaign: cria/atualiza contato, adiciona à
// lista Book Business, aplica tag de variant e seta o estágio do funil.
//
// POST /functions/v1/pv-lead
// {
//   nome: string,           // obrigatório
//   email: string,          // obrigatório
//   whatsapp?: string,
//   stage: "escrevendo" | "lancando" | "publicado",
//   variant: "checkout" | "lista",
//   utm_source?, utm_medium?, utm_campaign?, utm_content?, utm_term?,
//   lang?: "es"           // produto INTERNACIONAL (so preco): lista/tag proprias, sem field 68, sem forcar DDI 55
// }
//
// Black Week Motorizada 2026 (pagina /black-week): variant "black-week", sem stage obrigatorio.
// { nome, email, whatsapp, variant: "black-week", posicao, td_fase?, td_livro?, utm_* }
// -> lista 15 + tag 382 (BF-26); se ja for aluno do Metodo (RPC bw_eh_aluno) ganha tambem a tag 383 (BF-26-aluno).

// deno-lint-ignore-file no-explicit-any
import { serve } from "https://deno.land/std@0.224.0/http/server.ts";

const AC_API_URL = "https://amazing9rs.api-us1.com/api/3";
const AC_API_KEY = Deno.env.get("AC_API_KEY") ?? "";

// IDs descobertos via API (não mudam, mas centralizados pra fácil ajuste)
const LIST_ID = 6;                // Book Business (base mãe, 49k contatos)
const TAG_CHECKOUT = 181;         // Finalizou_Pre_Checkout (variant A)
const TAG_LISTA = 321;            // Finalizou_Pre_ListadeEspera (variant B)
const FIELD_ESTAGIO = 68;         // MTBB_ESTAGIO_FUNIL (dropdown)

const STAGES_VALID = new Set(["escrevendo", "lancando", "publicado"]);
const VARIANTS_VALID = new Set(["checkout", "lista"]);

// Black Week Motorizada 2026 (criados no AC em 2026-10-05)
const BW_LIST_ID = 15;            // lista "Black Week Motorizada 2026"
const BW_TAG_CADASTRO = 382;      // tag "BF-26" (cliente, 19/10; antes 380 bw-motorizada-cadastro)
const BW_TAG_ALUNO = 383;         // tag "BF-26-aluno" (ja comprou o Metodo; antes 381)
// 22/10: páginas de alunos (/black-week-alunos/ e /black-week-vitalicio/). Aluno = tag BF-26-aluno + automação 856.
// Vitalício: tag e automação próprias ainda não existem no AC (cliente cria); até lá recebe a BF-26-aluno e nenhuma automação.
const BW_TAG_VITALICIO = 385;      // "BF-26-vitalicio" (criada em 22/10)
const BW_AUTOMACAO_ALUNO = 856;    // "Confirmação Inscrição - ALUNO"
const BW_AUTOMACAO_VITALICIO = 0;  // TROCAR pela automação do AC quando o cliente criar
const BW_AUTOMACAO = 855;         // "[BF26] [OPERACIONAL] - Confirmação Inscrição" (cliente, 19/10): todo cadastro da página entra nela
const BW_FIELD_LIVRO = 122;       // campo "BW Livro (test drive)" (%BW_LIVRO%)
const BW_FASE_ESTAGIO: Record<string, string> = { construcao: "escrevendo", lancamento: "lancando", permanencia: "publicado" };
const SB_URL = Deno.env.get("SUPABASE_URL") ?? "";
const SB_SERVICE = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";

// ES (produto internacional, so preco): estrutura SEPARADA do BR. Preencher apos criar no AC.
const ES_LIST_ID: number | null = 13;          // lista "MTBB ES (internacional)" (criada 2026-09-08)
const ES_TAG_CHECKOUT: number | null = 360;    // tag "MTBB ES - Finalizou Pre Checkout" (criada 2026-09-08)
const ES_TAG_NAME_FALLBACK = "MTBB ES - Finalizou Pre Checkout"; // find-or-create se o id nao estiver setado

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization, x-client-info, apikey",
  "Access-Control-Max-Age": "86400",
};

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", ...CORS_HEADERS },
  });
}

async function acFetch(path: string, init: RequestInit = {}) {
  // 22/10: AC caiu (522) e derrubou o cadastro. Timeout de 8 s e erro de rede vira ok:false (status 0), nunca exceção.
  let r: Response;
  try { r = await fetch(`${AC_API_URL}${path}`, {
    ...init, signal: AbortSignal.timeout(8000),
    headers: {
      "Api-Token": AC_API_KEY,
      "Content-Type": "application/json",
      "Accept": "application/json",
      ...(init.headers || {}),
    },
  }); } catch (e) { return { ok: false, status: 0, data: null, text: String(e) }; }
  const text = await r.text().catch(() => "");
  let data: any = null;
  try { data = text ? JSON.parse(text) : null; } catch { /* keep null */ }
  return { ok: r.ok, status: r.status, data, text };
}

function normalizePhone(raw: string, intl = false): string {
  // Mantém só dígitos, prefixa 55 se for 10-11 dig (BR sem DDI). intl (ES): nunca força 55, aceita 8-15 dígitos.
  const d = (raw || "").replace(/\D+/g, "");
  if (!d) return "";
  if (intl) return d.length >= 8 && d.length <= 15 ? d : "";
  // 20/10: decide pelo NÚMERO DE DÍGITOS, nunca pelo começo (DDD 55 existe: Santa Maria/RS). 0 da operadora sai.
  // 11 = DDD+celular (mesmo começando com 55) · 12/13 começando com 55 = já tem DDI · 10 = DDD+8 (celular ganha o 9).
  let n = d.replace(/^0+/, "");
  if ((n.length === 12 || n.length === 13) && n.startsWith("55")) n = n.slice(2);
  if (n.length === 10 && /[6-9]/.test(n.charAt(2))) n = n.slice(0, 2) + "9" + n.slice(2);
  if (n.length === 10 || n.length === 11) return "55" + n;
  return d;
}

function sanitize(s: any, max = 200): string {
  return String(s ?? "").trim().slice(0, max);
}

// ---------------------------------------------------------------------------
// Black Week Motorizada 2026: cadastro da pagina /black-week
// ---------------------------------------------------------------------------
async function ehAluno(email: string): Promise<boolean> {
  if (!SB_URL || !SB_SERVICE) return false;
  try {
    const r = await fetch(`${SB_URL}/rest/v1/rpc/bw_eh_aluno`, {
      method: "POST",
      headers: { "Content-Type": "application/json", apikey: SB_SERVICE, Authorization: `Bearer ${SB_SERVICE}` },
      body: JSON.stringify({ p_email: email }),
    });
    return r.ok ? (await r.json()) === true : false;
  } catch { return false; } // nunca quebra o cadastro
}

// 22/10: aluno ou vitalício pela lista da Hotmart (tabela bf26_alunos). null = não é aluno. Erro de rede = deixa passar.
async function publicoDoEmail(email: string): Promise<string | null | undefined> {
  try {
    const r = await fetch(`${SB_URL}/rest/v1/rpc/bf26_publico`, {
      method: "POST", signal: AbortSignal.timeout(5000),
      headers: { "Content-Type": "application/json", apikey: SB_SERVICE, Authorization: `Bearer ${SB_SERVICE}` },
      body: JSON.stringify({ p_email: email }),
    });
    return r.ok ? await r.json() : undefined;
  } catch { return undefined; }
}

async function blackWeek(payload: any, nome: string, email: string, whatsapp: string) {
  // páginas de alunos: confere o e-mail ANTES de tudo. Fora da lista = 403 email_nao_aluno (a página mostra "Esse e-mail não é válido.").
  // Vitalício que cair na página de alunos passa (também é aluno); aluno normal na página do vitalício não passa.
  const publico = ["aluno", "vitalicio"].includes(String(payload.publico)) ? String(payload.publico) : "";
  if (publico) {
    const tipo = await publicoDoEmail(email);
    if (tipo !== undefined && (!tipo || (publico === "vitalicio" && tipo !== "vitalicio"))) return json({ error: "email_nao_aluno" }, 403);
  }
  const tagId = publico === "vitalicio" && BW_TAG_VITALICIO ? BW_TAG_VITALICIO : publico ? BW_TAG_ALUNO : BW_TAG_CADASTRO;
  const autoId = publico === "vitalicio" ? BW_AUTOMACAO_VITALICIO : publico ? BW_AUTOMACAO_ALUNO : BW_AUTOMACAO;
  const [firstName, ...rest] = nome.split(/\s+/);
  const estagio = BW_FASE_ESTAGIO[sanitize(payload.td_fase, 20)] || "";
  const livro = sanitize(payload.td_livro, 48);
  const fieldValues: any[] = [];
  if (estagio) fieldValues.push({ field: FIELD_ESTAGIO, value: estagio });
  if (livro) fieldValues.push({ field: BW_FIELD_LIVRO, value: livro });

  const sync = await acFetch("/contact/sync", { method: "POST", body: JSON.stringify({ contact: { email, firstName, lastName: rest.join(" "), phone: whatsapp || undefined, fieldValues } }) });
  // 22/10: AC fora do ar NÃO perde o cadastro: grava no Supabase com ac_contact_id nulo e a pessoa segue pro obrigado.
  // Quem ficou sem AC é reenviado depois (ac_contact_id is null).
  const contactId = sync.ok ? Number(sync.data?.contact?.id) || 0 : 0;
  const nada = { ok: false, status: 0, data: null, text: "ac_indisponivel" };
  const lista = !contactId ? nada : await acFetch("/contactLists", { method: "POST", body: JSON.stringify({ contactList: { list: BW_LIST_ID, contact: contactId, status: 1 } }) });
  // 19/10: a BF-26-aluno NÃO é aplicada aqui. Ela dispara a automação de alunos (856), que é da página de alunos
  // (ainda não feita). Na página do mistério todo mundo, aluno ou não, recebe a BF-26 e entra na automação 855.
  const aluno = await ehAluno(email);
  const tagAluno: boolean | null = null;
  const tag = !contactId ? nada : await acFetch("/contactTags", { method: "POST", body: JSON.stringify({ contactTag: { contact: contactId, tag: tagId } }) });
  const auto = !contactId || !autoId ? nada : await acFetch("/contactAutomations", { method: "POST", body: JSON.stringify({ contactAutomation: { contact: contactId, automation: autoId } }) });
  // 19/10: guarda o cadastro no Supabase para o dash da Black no Miolo (recadastro = nova linha). Nunca quebra o cadastro.
  try {
    const u = (k: string, n = 200) => sanitize(payload[k], n) || null;
    await fetch(`${SB_URL}/rest/v1/bf26_cadastros`, {
      method: "POST",
      headers: { "Content-Type": "application/json", apikey: SB_SERVICE, Authorization: `Bearer ${SB_SERVICE}`, Prefer: "return=minimal" },
      body: JSON.stringify({ email, nome, whatsapp: whatsapp || null, aluno, posicao: sanitize(payload.posicao, 20) || null,
        utm_source: u("utm_source"), utm_medium: u("utm_medium"), utm_campaign: u("utm_campaign"), utm_content: u("utm_content"),
        utm_term: u("utm_term"), utm_id: u("utm_id"), sck: u("sck"), fbclid: u("fbclid", 300), src: u("src"),
        ac_contact_id: contactId || null, automacao_ok: auto.ok,
        ab: ['A', 'B', 'C'].includes(String(payload.ab)) ? String(payload.ab) : null,   // 19/10: variante do teste A/B (só quem foi sorteado)
        obg: ['A', 'B', 'C', 'D'].includes(String(payload.obg)) ? String(payload.obg) : null, obg_tk: sanitize(payload.obg_tk, 32) || null, publico: publico || null }),   // 20/10: teste A/B da página de obrigado
    });
  } catch { /* o cadastro no AC já valeu */ }
  return json({
    ok: true, variant: "black-week", contact_id: contactId || null, ac_ok: !!contactId, ac_status: sync.status,
    list_added: lista.ok || lista.status === 422, tag_applied: tag.ok || tag.status === 422,
    // 422 = automação inativa (ou contato já dentro): o cadastro segue valendo, mas a confirmação não sai
    automation_added: auto.ok, automation_status: auto.status, automation_detail: auto.ok ? null : auto.text?.slice(0, 200),
    aluno, tag_aluno: tagAluno, estagio: estagio || null, posicao: sanitize(payload.posicao, 20),
  });
}

serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS_HEADERS });
  if (req.method !== "POST") return json({ error: "method_not_allowed" }, 405);
  if (!AC_API_KEY) return json({ error: "ac_key_not_configured" }, 500);

  let payload: any;
  try {
    payload = await req.json();
  } catch {
    return json({ error: "invalid_json" }, 400);
  }

  const nome = sanitize(payload.nome, 120);
  const email = sanitize(payload.email, 200).toLowerCase();
  const lang = sanitize(payload.lang, 5).toLowerCase();
  const isEs = lang === "es";
  // 20/10: a página manda "+<DDI>..." quando a pessoa escolhe outro país no seletor; aí não aplica a regra do Brasil
  const zapRaw = sanitize(payload.whatsapp, 30);
  const zapIntl = isEs || (/^\s*\+/.test(zapRaw) && !/^\s*\+\s*55/.test(zapRaw));
  const whatsapp = normalizePhone(zapRaw, zapIntl);
  const stage = sanitize(payload.stage, 30);
  const variant = sanitize(payload.variant, 30);

  if (!nome || nome.length < 2) return json({ error: "nome_invalid" }, 400);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ error: "email_invalid" }, 400);
  if (variant === "black-week") return blackWeek(payload, nome, email, whatsapp);
  if (!STAGES_VALID.has(stage)) return json({ error: "stage_invalid" }, 400);
  if (!VARIANTS_VALID.has(variant)) return json({ error: "variant_invalid" }, 400);

  const tagId = variant === "checkout" ? TAG_CHECKOUT : TAG_LISTA;

  // Split first/last name (AC usa firstName / lastName)
  const [firstName, ...rest] = nome.split(/\s+/);
  const lastName = rest.join(" ");

  // 1) Sync contact (upsert by email)
  const syncBody = {
    contact: {
      email,
      firstName,
      lastName,
      phone: whatsapp || undefined,
      fieldValues: isEs ? [] : [
        { field: FIELD_ESTAGIO, value: stage },
      ],
    },
  };
  const sync = await acFetch("/contact/sync", { method: "POST", body: JSON.stringify(syncBody) });
  if (!sync.ok) return json({ error: "ac_sync_failed", status: sync.status, detail: sync.text?.slice(0, 500) }, 502);

  const contactId = sync.data?.contact?.id;
  if (!contactId) return json({ error: "ac_no_contact_id", detail: sync.text?.slice(0, 500) }, 502);

  // 2) Add to list: BR -> 6 (Book Business); ES -> lista propria (se configurada)
  const targetList = isEs ? ES_LIST_ID : LIST_ID;
  let listOk: boolean | null = null;
  if (targetList) {
    const listRel = await acFetch("/contactLists", {
      method: "POST",
      body: JSON.stringify({ contactList: { list: targetList, contact: Number(contactId), status: 1 } }),
    });
    listOk = listRel.ok || listRel.status === 422; // 422 = ja estava na lista
  }

  // 3) Apply tag: BR -> 181/321; ES -> tag propria (id ou find-or-create por nome; nunca deixa lead ES sem marca)
  let useTag: number | null = isEs ? ES_TAG_CHECKOUT : tagId;
  if (isEs && !useTag) {
    try {
      const f = await acFetch("/tags?search=" + encodeURIComponent(ES_TAG_NAME_FALLBACK));
      if (f.ok) { const t = (f.data?.tags || []).find((x: any) => x.tag === ES_TAG_NAME_FALLBACK); if (t) useTag = Number(t.id); }
      if (!useTag) {
        const c = await acFetch("/tags", { method: "POST", body: JSON.stringify({ tag: { tag: ES_TAG_NAME_FALLBACK, tagType: "contact", description: "Lead ES (produto internacional) que finalizou o pre-checkout" } }) });
        useTag = c.data?.tag?.id ? Number(c.data.tag.id) : null;
      }
    } catch { /* nunca quebra o lead */ }
  }
  let tagOk: boolean | null = null;
  if (useTag) {
    const tagRel = await acFetch("/contactTags", { method: "POST", body: JSON.stringify({ contactTag: { contact: Number(contactId), tag: useTag } }) });
    tagOk = tagRel.ok || tagRel.status === 422;
  }

  // Pega UTMs e outros metadados pra eventual storage interno futuro
  const utms = {
    utm_source: sanitize(payload.utm_source, 100),
    utm_medium: sanitize(payload.utm_medium, 100),
    utm_campaign: sanitize(payload.utm_campaign, 100),
    utm_content: sanitize(payload.utm_content, 100),
    utm_term: sanitize(payload.utm_term, 100),
  };

  // 4) Origem: marca "veio de anúncio" pra segmentar no AC (find-or-create da tag; nunca quebra o lead)
  const src = sanitize(payload.src, 200);
  const isPaid = /^ppto-/i.test(src) || /(facebook|meta)/i.test(utms.utm_source) || /(cpc|paid|ads)/i.test(utms.utm_medium);
  let paidTagOk: boolean | null = null;
  if (isPaid) {
    try {
      const TAG_NAME = isEs ? "MTBB ES - Trafego pago" : "MTBB - Tráfego pago";
      let adTagId: number | null = null;
      const found = await acFetch("/tags?search=" + encodeURIComponent(TAG_NAME));
      if (found.ok) { const t = (found.data?.tags || []).find((x: any) => x.tag === TAG_NAME); if (t) adTagId = Number(t.id); }
      if (!adTagId) {
        const created = await acFetch("/tags", { method: "POST", body: JSON.stringify({ tag: { tag: TAG_NAME, tagType: "contact", description: "Lead que veio de anúncio (Meta) — perpétuo" } }) });
        adTagId = created.data?.tag?.id ? Number(created.data.tag.id) : null;
      }
      if (adTagId) {
        const r = await acFetch("/contactTags", { method: "POST", body: JSON.stringify({ contactTag: { contact: Number(contactId), tag: adTagId } }) });
        paidTagOk = r.ok || r.status === 422;
      }
    } catch { /* nunca quebra o lead */ }
  }

  return json({
    ok: true,
    contact_id: contactId,
    list_added: listOk,
    tag_applied: tagOk,
    paid: isPaid,
    paid_tag: paidTagOk,
    variant,
    stage,
    lang: isEs ? "es" : "pt",
    utms,
  });
});
