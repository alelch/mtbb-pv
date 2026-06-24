-- ============================================================
-- Segurança do admin.html — senha validada no SERVIDOR (Supabase)
-- Deploy: Supabase -> SQL Editor -> Run. Projeto jsqtpsxpaclslakafmvd.
--
-- ⚠️ TROQUE a senha no passo 1 por uma FORTE antes de rodar.
-- A senha NÃO fica no código da página: o front só a envia; o banco valida.
-- Sem a senha certa, as métricas nem são retornadas.
-- ============================================================

-- 1) Cofre da senha. RLS sem policy = ninguém (anon/authenticated) lê direto;
--    só as funções SECURITY DEFINER abaixo conseguem consultar.
create table if not exists public.mtbb_admin_secret (
  id   int primary key default 1,
  pass text not null
);
alter table public.mtbb_admin_secret enable row level security;
revoke all on public.mtbb_admin_secret from anon, authenticated;

-- >>>>> DEFINA SUA SENHA FORTE AQUI (troque o valor) <<<<<
insert into public.mtbb_admin_secret (id, pass)
values (1, 'TROQUE_POR_UMA_SENHA_FORTE')
on conflict (id) do update set pass = excluded.pass;

-- 2) Verificador de senha (login)
create or replace function public.mtbb_admin_ok(p_pass text)
returns boolean
language sql security definer set search_path = public as $$
  select exists (
    select 1 from public.mtbb_admin_secret where id = 1 and pass = p_pass
  );
$$;
grant execute on function public.mtbb_admin_ok(text) to anon;

-- 3) Métricas (gated): só retorna dados se a senha bater
create or replace function public.mtbb_admin_metrics(p_pass text, p_since timestamptz)
returns json
language plpgsql security definer set search_path = public as $$
begin
  if not public.mtbb_admin_ok(p_pass) then
    raise exception 'unauthorized' using errcode = '42501';
  end if;
  return json_build_object(
    'global',   (select row_to_json(g) from public.mtbb_pv_global_get(p_since) g),
    'funnel',   (select coalesce(json_agg(f), '[]'::json) from public.mtbb_pv_funnel_get(p_since) f),
    'obrigado', (select coalesce(json_agg(o), '[]'::json) from public.mtbb_pv_obrigado_get(p_since) o),
    'metodo_vendas', (
      -- Compras do Método (Hotmart) reaproveitando a tabela vendas (webhook existente).
      -- attr_n = vendas atribuídas ao funil via sck=preco-<estágio> (vem no payload_raw).
      select json_build_object(
        'attr_n',  count(*) filter (where sck ~ '^preco-(escrevendo|lancando|publicado)$'),
        'total_n', count(*),
        'receita', coalesce(sum(valor), 0)
      )
      from (
        select valor, coalesce(
          payload_raw->'data'->'purchase'->'tracking'->>'source_sck',
          payload_raw->'data'->'purchase'->'tracking'->>'sck',
          payload_raw->'data'->'purchase'->'tracking'->>'source'
        ) as sck
        from public.vendas
        where produto_codigo = 'PPTO'
          and created_at >= p_since
          and upper(coalesce(status, '')) in ('APPROVED', 'COMPLETE', 'COMPLETED')
      ) s
    )
  );
end $$;
grant execute on function public.mtbb_admin_metrics(text, timestamptz) to anon;

-- 4) Gravar config de roteamento (gated). Faz upsert direto (não depende da
--    função antiga). As 3 linhas de estágio já existem, então cai no UPDATE.
create or replace function public.mtbb_admin_set_config(
  p_pass text, p_escrevendo int, p_lancando int, p_publicado int
) returns boolean
language plpgsql security definer set search_path = public as $$
begin
  if not public.mtbb_admin_ok(p_pass) then
    raise exception 'unauthorized' using errcode = '42501';
  end if;

  update public.mtbb_pv_config set preco_pct = p_escrevendo, updated_at = now() where stage = 'escrevendo';
  if not found then insert into public.mtbb_pv_config (stage, preco_pct, updated_at) values ('escrevendo', p_escrevendo, now()); end if;

  update public.mtbb_pv_config set preco_pct = p_lancando, updated_at = now() where stage = 'lancando';
  if not found then insert into public.mtbb_pv_config (stage, preco_pct, updated_at) values ('lancando', p_lancando, now()); end if;

  update public.mtbb_pv_config set preco_pct = p_publicado, updated_at = now() where stage = 'publicado';
  if not found then insert into public.mtbb_pv_config (stage, preco_pct, updated_at) values ('publicado', p_publicado, now()); end if;

  return true;
end $$;
grant execute on function public.mtbb_admin_set_config(text, int, int, int) to anon;

-- 5) Fecha as leituras de métricas pro anon: só passam pelo wrapper gated.
--    Bloco dinâmico = robusto a qualquer assinatura (não precisa cravar o tipo).
--    (As funções continuam existindo; o wrapper SECURITY DEFINER as chama.)
do $$
declare r record;
begin
  for r in
    select p.oid::regprocedure as sig
    from pg_proc p
    where p.pronamespace = 'public'::regnamespace
      and p.proname in ('mtbb_pv_global_get', 'mtbb_pv_funnel_get', 'mtbb_pv_obrigado_get')
  loop
    -- revoga de PUBLIC tambem (grant default do Postgres), senao anon mantem acesso
    execute 'revoke execute on function ' || r.sig || ' from public, anon, authenticated';
  end loop;
end $$;

-- Observação: a tabela mtbb_pv_config continua legível por anon de propósito
-- (o quiz público precisa das % de roteamento; elas não são sensíveis).

-- 6) Zerar métricas do funil/teste A-B (gated). Apaga TODOS os eventos de
--    tracking (mtbb_pv_events). NÃO toca em vendas (Hotmart). Usado pelo botão
--    "Zerar métricas" do admin. Já deployada via Management API.
create or replace function public.mtbb_admin_reset_metrics(p_pass text)
returns json language plpgsql security definer set search_path = public as $$
declare n bigint;
begin
  if not public.mtbb_admin_ok(p_pass) then
    raise exception 'unauthorized' using errcode = '42501';
  end if;
  delete from public.mtbb_pv_events;
  get diagnostics n = row_count;
  return json_build_object('deleted', n);
end $$;
grant execute on function public.mtbb_admin_reset_metrics(text) to anon;
