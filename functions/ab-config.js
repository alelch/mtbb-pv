/**
 * Config do A/B servida pelo PRÓPRIO domínio (Cloudflare Pages Function).
 *
 * Por que existe: a página lia a config direto do Supabase, e bloqueadores derrubam
 * `*.supabase.co`. Isso obrigava a manter uma cópia da config dentro do HTML (o FALLBACK),
 * que precisava de deploy toda vez que um teste mudava — e em 12/08/2026 ficou desatualizada
 * (o vencedor já estava marcado no dash e o HTML ainda mandava 80/20).
 * Servindo do mesmo domínio, o bloqueador não tem o que bloquear: a config nunca fica velha.
 *
 * Uso: /ab-config?pagina=lancamento-v1  → [{slug,escopo,sck_tag,vencedor,variantes}]
 * Só testes ATIVOS. Cache de 60s na borda (config muda pouco; 1 min de atraso é aceitável).
 */
const SB = 'https://jsqtpsxpaclslakafmvd.supabase.co';
const AK = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpzcXRwc3hwYWNsc2xha2FmbXZkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUzMTY5NTMsImV4cCI6MjA5MDg5Mjk1M30.6f3CmgozaE3fTORF0SBSeRDzZNZ1E27tcdQ9h6tKLgc';

export async function onRequestGet({ request }) {
  const pagina = new URL(request.url).searchParams.get('pagina') || '';
  const headers = {
    'content-type': 'application/json; charset=utf-8',
    'cache-control': 'public, max-age=30, s-maxage=60',
    'access-control-allow-origin': '*'
  };
  if (!/^[a-z0-9-]{1,40}$/i.test(pagina)) {
    return new Response('[]', { headers });
  }
  try {
    const url = SB + '/rest/v1/ab_testes?pagina=eq.' + encodeURIComponent(pagina) +
      '&ativo=eq.true&select=slug,escopo,sck_tag,vencedor,variantes';
    const r = await fetch(url, { headers: { apikey: AK, Authorization: 'Bearer ' + AK } });
    if (!r.ok) return new Response('[]', { headers });
    return new Response(await r.text(), { headers });
  } catch (e) {
    return new Response('[]', { headers });   // falha → a página cai no cache local / fallback
  }
}
