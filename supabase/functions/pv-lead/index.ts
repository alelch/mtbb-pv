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
//   utm_source?, utm_medium?, utm_campaign?, utm_content?, utm_term?
// }

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
  const r = await fetch(`${AC_API_URL}${path}`, {
    ...init,
    headers: {
      "Api-Token": AC_API_KEY,
      "Content-Type": "application/json",
      "Accept": "application/json",
      ...(init.headers || {}),
    },
  });
  const text = await r.text();
  let data: any = null;
  try { data = text ? JSON.parse(text) : null; } catch { /* keep null */ }
  return { ok: r.ok, status: r.status, data, text };
}

function normalizePhone(raw: string): string {
  // Mantém só dígitos, prefixa 55 se for 10-11 dig (BR sem DDI)
  const d = (raw || "").replace(/\D+/g, "");
  if (!d) return "";
  if (d.length >= 12 && d.length <= 13) return d;          // já tem DDI
  if (d.length === 10 || d.length === 11) return "55" + d;  // adiciona DDI BR
  return d;
}

function sanitize(s: any, max = 200): string {
  return String(s ?? "").trim().slice(0, max);
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
  const whatsapp = normalizePhone(sanitize(payload.whatsapp, 30));
  const stage = sanitize(payload.stage, 30);
  const variant = sanitize(payload.variant, 30);

  if (!nome || nome.length < 2) return json({ error: "nome_invalid" }, 400);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ error: "email_invalid" }, 400);
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
      fieldValues: [
        { field: FIELD_ESTAGIO, value: stage },
      ],
    },
  };
  const sync = await acFetch("/contact/sync", { method: "POST", body: JSON.stringify(syncBody) });
  if (!sync.ok) return json({ error: "ac_sync_failed", status: sync.status, detail: sync.text?.slice(0, 500) }, 502);

  const contactId = sync.data?.contact?.id;
  if (!contactId) return json({ error: "ac_no_contact_id", detail: sync.text?.slice(0, 500) }, 502);

  // 2) Add to list 6 (Book Business)
  const listRel = await acFetch("/contactLists", {
    method: "POST",
    body: JSON.stringify({ contactList: { list: LIST_ID, contact: Number(contactId), status: 1 } }),
  });
  // status 1 = subscribed; AC retorna 201 ou 422 se já estiver (ok ambos)
  const listOk = listRel.ok || listRel.status === 422;

  // 3) Apply tag
  const tagRel = await acFetch("/contactTags", {
    method: "POST",
    body: JSON.stringify({ contactTag: { contact: Number(contactId), tag: tagId } }),
  });
  const tagOk = tagRel.ok || tagRel.status === 422;

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
      const TAG_NAME = "MTBB - Tráfego pago";
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
    utms,
  });
});
