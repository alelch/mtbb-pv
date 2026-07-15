// pv-click: grava o contexto do clique de checkout (fbc/fbp + IP/UA do visitante)
// keyado pelo vid curto que a página embute no sck (|v<id>).
// O nó "Meta CAPI Purchase" do n8n cruza na venda e enriquece o user_data do Purchase.
// Chamada como "simple request" (sem Content-Type json) pra não ter preflight CORS.
Deno.serve(async (req) => {
  const cors = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "content-type",
  };
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return new Response("pv-click up", { headers: cors });
  try {
    const body = JSON.parse(await req.text());
    const vid = String(body.vid || "");
    if (!/^[a-z0-9]{6,20}$/.test(vid)) return new Response("bad vid", { status: 400, headers: cors });
    const fbc = typeof body.fbc === "string" ? body.fbc.slice(0, 255) : null;
    const fbp = typeof body.fbp === "string" ? body.fbp.slice(0, 64) : null;
    const ip = (req.headers.get("x-forwarded-for") || "").split(",")[0].trim() || null;
    const ua = (req.headers.get("user-agent") || "").slice(0, 512) || null;
    const url = Deno.env.get("SUPABASE_URL");
    const key = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    const res = await fetch(`${url}/rest/v1/click_context?on_conflict=vid`, {
      method: "POST",
      headers: {
        apikey: key!, Authorization: `Bearer ${key}`, "Content-Type": "application/json",
        Prefer: "resolution=merge-duplicates,return=minimal",
      },
      body: JSON.stringify({ vid, fbc, fbp, ip, ua, updated_at: new Date().toISOString() }),
    });
    return new Response(res.ok ? "ok" : "db err", { status: res.ok ? 200 : 500, headers: cors });
  } catch {
    return new Response("err", { status: 400, headers: cors });
  }
});
