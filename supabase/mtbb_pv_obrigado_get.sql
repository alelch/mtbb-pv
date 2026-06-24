-- Teste A/B/C da página de obrigado da lista de espera (carta/bento/conversa).
-- Agrega por meta.obrigado_variant: visitantes únicos que VIRAM (obrigado_view)
-- e que CLICARAM no WhatsApp (whatsapp_click). Dedup por session_id.
-- SECURITY DEFINER porque o anon não pode dar SELECT direto em mtbb_pv_events (RLS).
--
-- Deploy: cole no Supabase → SQL Editor → Run. Projeto jsqtpsxpaclslakafmvd.

create or replace function public.mtbb_pv_obrigado_get(p_since timestamptz)
returns table (
  variant text,
  views bigint,
  converters bigint
)
language sql
security definer
set search_path = public
as $$
  select
    e.meta->>'obrigado_variant' as variant,
    count(distinct e.session_id) filter (where e.event_type = 'obrigado_view')   as views,
    count(distinct e.session_id) filter (where e.event_type = 'whatsapp_click')  as converters
  from public.mtbb_pv_events e
  where e.created_at >= p_since
    and e.event_type in ('obrigado_view', 'whatsapp_click')
    and e.meta ? 'obrigado_variant'
    and e.meta->>'obrigado_variant' is not null
  group by 1
  order by 1;
$$;

-- NÃO conceder execute pro anon: esta RPC é chamada só internamente pelo wrapper
-- SECURITY DEFINER mtbb_admin_metrics (roda como owner). O acesso anon foi revogado
-- em admin_security.sql; manter o grant aqui reabriria o buraco ao reaplicar.
