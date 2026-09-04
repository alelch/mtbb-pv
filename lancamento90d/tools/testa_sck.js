// Prova que o clique sai carimbado com a variante no sck e com a query string
// da pagina colada (que e o que mantem o 1 clique da Hotmart funcionando).
const fs=require('fs'), vm=require('vm');
const CODE=fs.readFileSync('/Users/alexandrechmatailk/Claude Code/mtbb-pv/lancamento90d/assets/oferta.js','utf8');

function clica({variante, off, search, aoVivo=true}){
  let foi=null, cookies={}, handler=null;
  const alvo={hasAttribute:n=>n==='data-aceita', setAttribute(){}, style:{}, textContent:''};
  const doc={ addEventListener:(t,f)=>{handler=f;}, querySelectorAll:()=>[] };
  Object.defineProperty(doc,'cookie',{get(){return Object.entries(cookies).map(([k,v])=>k+'='+v).join('; ');},
    set(v){const [kv]=v.split(';');const[k,val]=kv.split('=');cookies[k]=val;}});
  const loc={search, hash:'', replace(){},
    get href(){return 'https://x.test/lancamento90d/upsell/'+search;}, set href(u){foi=u;}};
  const win={ OFERTA:{variante, preco:1, aceite:'https://pay.hotmart.com/A107472443R?off='+off,
    recusa:'https://obrigado.test/x', outraUrl: variante==='A'?'../upsell-b/':undefined,
    sku:'S', valor:1, sckTag:'pd', AO_VIVO:aoVivo}, location:loc, document:doc };
  const ctx={window:win, document:doc, location:loc, Math:{...Math, random:()=>variante==='A'?0.1:0.9},
    URL, URLSearchParams, Date};
  vm.createContext(ctx); vm.runInContext(CODE, ctx);
  handler({target:{closest:()=>alvo}, preventDefault(){}});
  return foi;
}
const a=clica({variante:'A', off:'n740dj0b', search:'?tk=ABC&email=a%40b.com&src=L90D'});
const b=clica({variante:'B', off:'8rn7djuk', search:'?tk=ABC&email=a%40b.com&src=L90D'});
console.log('A ->', a);
console.log('B ->', b);
const ok = a.includes('off=n740dj0b') && a.includes('sck=pdA') && a.includes('tk=ABC') && a.includes('email=a%40b.com')
        && b.includes('off=8rn7djuk') && b.includes('sck=pdB') && b.includes('tk=ABC');
console.log(ok ? '\nok: oferta certa + marcador certo + query string preservada' : '\nFALHOU');
