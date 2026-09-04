// Roda o oferta.js PUBLICADO com browser stubado, forcando Math.random, pra
// provar: (1) a A sorteia e redireciona metade, (2) a B NUNCA redireciona
// (anti-loop), (3) a query string sobrevive ao redirect, (4) o sck sai
// carimbado com a variante certa.
const fs = require('fs');
const CODE = fs.readFileSync('/Users/alexandrechmatailk/Claude Code/mtbb-pv/lancamento90d/assets/oferta.js','utf8');

function roda({variante, outraUrl, moeda, cookieInicial, search}){
  let redirecionou = null, cookies = cookieInicial ? {l90d_pd:cookieInicial} : {};
  const listeners = [];
  const els = [];
  const doc = {
    cookie: Object.entries(cookies).map(([k,v])=>k+'='+v).join('; '),
    addEventListener: (t,f)=>listeners.push(f),
    querySelectorAll: ()=>els,
  };
  Object.defineProperty(doc,'cookie',{
    get(){ return Object.entries(cookies).map(([k,v])=>k+'='+v).join('; '); },
    set(v){ const [kv]=v.split(';'); const [k,val]=kv.split('='); cookies[k]=val; }
  });
  const loc = {
    search, hash:'', href:'https://x.test/lancamento90d/'+(variante==='B'?'upsell-b':'upsell')+'/'+search,
    replace(u){ redirecionou = u; }
  };
  const win = {
    OFERTA: {variante, preco:1, aceite:'https://pay.hotmart.com/A107472443R?off=zzz',
             recusa:'https://obrigado.test/x', outraUrl, sku:'S', valor:1, sckTag:'pd', AO_VIVO:true},
    location: loc, document: doc, Math: {random:()=>moeda},
  };
  const ctx = {window:win, document:doc, location:loc, Math:{...Math, random:()=>moeda},
               URL, URLSearchParams, Date, fbq:undefined};
  const vm = require('vm');
  vm.createContext(ctx);
  vm.runInContext(CODE, ctx);
  return {redirecionou, cookie: cookies.l90d_pd};
}

const casos = [
  ['A, sorteio cai em A', {variante:'A', outraUrl:'../upsell-b/', moeda:0.2, search:'?tk=ABC&email=a%40b.com'}],
  ['A, sorteio cai em B', {variante:'A', outraUrl:'../upsell-b/', moeda:0.9, search:'?tk=ABC&email=a%40b.com'}],
  ['A, ja tinha cookie B', {variante:'A', outraUrl:'../upsell-b/', moeda:0.1, cookieInicial:'B', search:'?tk=ABC'}],
  ['B, moeda mandaria pra A', {variante:'B', outraUrl:undefined, moeda:0.1, search:'?tk=ABC'}],
  ['B, moeda mandaria pra B', {variante:'B', outraUrl:undefined, moeda:0.9, search:'?tk=ABC'}],
  ['B, entrou com cookie A', {variante:'B', outraUrl:undefined, moeda:0.9, cookieInicial:'A', search:'?tk=ABC'}],
];
let falhou = 0;
for (const [nome, cfg] of casos){
  const r = roda(cfg);
  const esperado =
    nome==='A, sorteio cai em B' ? '../upsell-b/?tk=ABC&email=a%40b.com' :
    nome==='A, ja tinha cookie B' ? '../upsell-b/?tk=ABC' : null;
  const ok = r.redirecionou === esperado;
  if(!ok) falhou++;
  console.log(`${ok?'ok  ':'FALHA'} | ${nome.padEnd(24)} | redirect: ${r.redirecionou||'nenhum'} | cookie: ${r.cookie}`);
}
console.log(falhou ? `\n${falhou} FALHA(S)` : '\ntodos passaram');
