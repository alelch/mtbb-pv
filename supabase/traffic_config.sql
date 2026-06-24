-- ============================================================
-- Roteador de tráfego — 3 distribuições nomeadas (quiz, pagina, obrigado)
-- Substitui a lógica antiga de preço/lista POR ESTÁGIO (mtbb_pv_config) por:
--   quiz     = % de fundo da porta  {a,b,c}
--   pagina   = % preço vs lista GLOBAL (vale pros 3 estágios) {preco,lista}
--   obrigado = % das páginas de obrigado {carta,bento,conversa}
-- Deploy: aplicado via Management API (NÃO roda o arquivo de senha junto).
-- ============================================================

create table if not exists public.mtbb_traffic_config (
  key        text primary key,          -- 'quiz' | 'pagina' | 'obrigado'
  dist       jsonb not null,            -- ex: {"a":34,"b":33,"c":33}
  updated_at timestamptz not null default now()
);

alter table public.mtbb_traffic_config enable row level security;

-- Leitura pública (as páginas precisam dos %): não é sensível.
drop policy if exists "traffic_anon_read" on public.mtbb_traffic_config;
create policy "traffic_anon_read" on public.mtbb_traffic_config
  for select to anon, authenticated using (true);
grant select on public.mtbb_traffic_config to anon, authenticated;

-- Seed inicial (não sobrescreve se já existir).
insert into public.mtbb_traffic_config (key, dist) values
  ('quiz',     '{"a":34,"b":33,"c":33}'::jsonb),
  ('pagina',   '{"preco":50,"lista":50}'::jsonb),
  ('obrigado', '{"carta":34,"bento":33,"conversa":33}'::jsonb)
on conflict (key) do nothing;

-- Gravar as 3 distribuições (gated por senha do admin).
create or replace function public.mtbb_admin_set_traffic(
  p_pass text, p_quiz jsonb, p_pagina jsonb, p_obrigado jsonb
) returns boolean
language plpgsql security definer set search_path = public as $$
begin
  if not public.mtbb_admin_ok(p_pass) then
    raise exception 'unauthorized' using errcode = '42501';
  end if;
  insert into public.mtbb_traffic_config (key, dist, updated_at) values
    ('quiz',     p_quiz,     now()),
    ('pagina',   p_pagina,   now()),
    ('obrigado', p_obrigado, now())
  on conflict (key) do update set dist = excluded.dist, updated_at = now();
  return true;
end $$;
grant execute on function public.mtbb_admin_set_traffic(text, jsonb, jsonb, jsonb) to anon;
