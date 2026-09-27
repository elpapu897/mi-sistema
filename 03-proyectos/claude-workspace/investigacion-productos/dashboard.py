#!/usr/bin/env python3
"""Genera dashboard.html (interactivo, autocontenido) desde productos_top50.json."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(BASE, "productos_top50.json"), encoding="utf-8"))
P = d["productos"]

datos = json.dumps(P, ensure_ascii=False).replace("</", "<\\/")
meta = json.dumps({k: d[k] for k in ("generado", "total_crudo", "total_filtrado", "descartes", "rate_ars")},
                  ensure_ascii=False).replace("</", "<\\/")

HTML = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Top 50 productos · salud, belleza y cuidado personal</title>
<style>
:root{
  --bg:#0d0f13; --panel:#151922; --panel2:#1c2130; --line:#252b38;
  --tx:#e8ecf4; --dim:#8b93a7; --acc:#5b8cff; --ok:#3ecf8e; --warn:#ffb340; --bad:#ff6b6b;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
  font:14px/1.5 -apple-system,BlinkMacSystemFont,"SF Pro Text","Inter",system-ui,sans-serif}
header{padding:28px 32px 20px;border-bottom:1px solid var(--line);
  background:linear-gradient(180deg,#171b25,#0d0f13)}
h1{margin:0 0 6px;font-size:24px;font-weight:650;letter-spacing:-.02em}
.sub{color:var(--dim);font-size:13px}
.kpis{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 16px;min-width:112px}
.kpi b{display:block;font-size:20px;font-weight:650;letter-spacing:-.02em}
.kpi span{font-size:11px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em}

.bar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;
  padding:14px 32px;border-bottom:1px solid var(--line);background:var(--panel);
  position:sticky;top:0;z-index:20}
input,select{background:var(--panel2);color:var(--tx);border:1px solid var(--line);
  border-radius:8px;padding:8px 11px;font:inherit;font-size:13px;outline:none}
input:focus,select:focus{border-color:var(--acc)}
#q{flex:1;min-width:200px}
.count{color:var(--dim);font-size:12px;margin-left:auto;white-space:nowrap}
button.reset{background:none;border:1px solid var(--line);color:var(--dim);
  border-radius:8px;padding:8px 12px;cursor:pointer;font:inherit;font-size:13px}
button.reset:hover{color:var(--tx);border-color:var(--acc)}

table{width:100%;border-collapse:collapse}
thead th{position:sticky;top:57px;background:var(--panel);z-index:10;
  text-align:left;font-size:11px;letter-spacing:.06em;text-transform:uppercase;
  color:var(--dim);font-weight:600;padding:11px 10px;border-bottom:1px solid var(--line);
  cursor:pointer;user-select:none;white-space:nowrap}
thead th:hover{color:var(--tx)}
thead th.num{text-align:right}
th .ar{opacity:.4;font-size:9px}
tbody td{padding:10px;border-bottom:1px solid var(--line);vertical-align:middle}
tbody tr{cursor:pointer}
tbody tr:hover{background:var(--panel)}
td.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.rank{color:var(--dim);font-size:12px;width:34px;text-align:right}
img.th{width:44px;height:44px;object-fit:cover;border-radius:7px;background:var(--panel2);display:block}
.tt{max-width:400px}
.tt a{color:var(--tx);text-decoration:none;font-weight:500}
.tt a:hover{color:var(--acc)}
.cat{color:var(--dim);font-size:11.5px;margin-top:2px}
.tag{display:inline-block;padding:2px 8px;border-radius:20px;font-size:11px;font-weight:600}
.n-Dolor{background:#3b2a52;color:#c9a8ff}.n-Piel{background:#123a44;color:#6fe0e8}
.n-Sueno{background:#1d3157;color:#8fb4ff}.n-Higiene{background:#0f3b2e;color:#5fe0a8}
.n-Salud-femenina{background:#4a1f38;color:#ff9ec7}.n-Salud-bebe{background:#4a3a14;color:#ffd27a}
.n-Cuidado-intimo{background:#37294d;color:#bda6ff}.n-Afeitado{background:#2b3340;color:#a8bcd8}
.n-Depilacion{background:#442436;color:#ff9fd0}.n-Belleza{background:#43293f;color:#f0a8e0}
.n-Cabello{background:#333;color:#ddd}.n-Barba{background:#333;color:#ddd}
.c-Baja{color:var(--ok)}.c-Media{color:var(--warn)}.c-Alta{color:var(--bad)}
.score{display:inline-flex;align-items:center;justify-content:center;
  min-width:44px;padding:4px 8px;border-radius:7px;font-weight:700;font-size:13px}
.s-a{background:rgba(62,207,142,.16);color:var(--ok)}
.s-b{background:rgba(91,140,255,.16);color:#8fb4ff}
.s-c{background:rgba(255,179,64,.16);color:var(--warn)}
.mult{color:var(--dim);font-size:11px}
.fast{color:var(--ok)}.slow{color:var(--warn)}

tr.det td{background:#10141c;padding:0}
.det-in{padding:16px 20px 20px 88px;display:none}
.det-in.open{display:block}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin-bottom:14px}
.f{background:var(--panel2);border:1px solid var(--line);border-radius:9px;padding:10px 12px}
.f span{display:block;font-size:10.5px;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.f b{font-size:15px;font-weight:600}
.note{font-size:12.5px;color:var(--dim);line-height:1.6}
.note b{color:var(--tx)}
.btn{display:inline-block;margin-top:10px;background:var(--acc);color:#fff;text-decoration:none;
  padding:8px 15px;border-radius:8px;font-size:13px;font-weight:600}
.btn:hover{filter:brightness(1.12)}
.warn-box{background:rgba(255,179,64,.1);border:1px solid rgba(255,179,64,.3);
  border-radius:8px;padding:9px 12px;font-size:12.5px;color:#ffd9a0;margin-bottom:12px}

footer{padding:26px 32px 44px;color:var(--dim);font-size:12.5px;line-height:1.75;
  border-top:1px solid var(--line);margin-top:24px}
footer h3{color:var(--tx);font-size:14px;margin:0 0 8px}
footer table{width:auto;margin:10px 0 18px}
footer td,footer th{padding:5px 18px 5px 0;border:none;text-align:left;font-size:12.5px}
footer th{color:var(--dim);font-weight:600;border-bottom:1px solid var(--line)}
.pill{display:inline-block;padding:1px 7px;border-radius:5px;font-size:11px;font-weight:600}
.real{background:rgba(62,207,142,.16);color:var(--ok)}
.est{background:rgba(255,179,64,.16);color:var(--warn)}
.empty{padding:60px;text-align:center;color:var(--dim)}
</style>
</head>
<body>
<header>
  <h1>Top 50 · salud, belleza y cuidado personal</h1>
  <div class="sub">Filtrado desde <b id="crudo"></b> productos del catálogo de proveedor ·
     <span id="fecha"></span></div>
  <div class="kpis">
    <div class="kpi"><b id="k1"></b><span>califican</span></div>
    <div class="kpi"><b id="k2"></b><span>coste medio</span></div>
    <div class="kpi"><b id="k3"></b><span>margen medio</span></div>
    <div class="kpi"><b id="k4"></b><span>múltiplo medio</span></div>
    <div class="kpi"><b id="k5"></b><span>competencia baja</span></div>
    <div class="kpi"><b id="k6"></b><span>envío rápido</span></div>
  </div>
</header>

<div class="bar">
  <input id="q" placeholder="Buscar producto…">
  <select id="fn"><option value="">Todos los nichos</option></select>
  <select id="fc"><option value="">Toda competencia</option>
    <option>Baja</option><option>Media</option><option>Alta</option></select>
  <select id="fe"><option value="">Todo envío</option>
    <option value="fast">Rápido (15-25 d)</option><option value="slow">Lento (25-45 d)</option></select>
  <select id="fp"><option value="">Todo precio</option>
    <option value="0-10">$5 – $10</option><option value="10-20">$10 – $20</option>
    <option value="20-99">$20 – $30</option></select>
  <button class="reset" id="rs">Limpiar</button>
  <span class="count" id="cnt"></span>
</div>

<table>
<thead><tr>
  <th></th><th></th>
  <th data-k="titulo">Producto <span class="ar"></span></th>
  <th data-k="nicho">Nicho <span class="ar"></span></th>
  <th class="num" data-k="coste">Coste <span class="ar"></span></th>
  <th class="num" data-k="pvp_sugerido">PVP <span class="ar"></span></th>
  <th class="num" data-k="margen_usd">Margen <span class="ar"></span></th>
  <th class="num" data-k="vendidos">Vendidos <span class="ar"></span></th>
  <th class="num" data-k="rating">★ <span class="ar"></span></th>
  <th data-k="competencia">Competencia <span class="ar"></span></th>
  <th data-k="envio">Envío <span class="ar"></span></th>
  <th class="num" data-k="score">Nota <span class="ar"></span></th>
</tr></thead>
<tbody id="tb"></tbody>
</table>
<div class="empty" id="empty" style="display:none">Ningún producto coincide con esos filtros.</div>

<footer>
  <h3>Cómo leer esta tabla (importante antes de comprar stock)</h3>
  <p>No todas las columnas valen lo mismo. Unas son dato verificado del catálogo y otras son
  estimación mía. Te lo separo para que no compres en base a un número que inventé:</p>
  <table>
    <tr><th>Columna</th><th>Origen</th><th>Confianza</th></tr>
    <tr><td>Coste</td><td>Precio real del catálogo</td><td><span class="pill real">dato</span></td></tr>
    <tr><td>Vendidos</td><td>Contador real de unidades vendidas</td><td><span class="pill real">dato</span></td></tr>
    <tr><td>★ Rating</td><td>Valoración real de compradores</td><td><span class="pill real">dato</span></td></tr>
    <tr><td>Envío</td><td>Según si el producto es <b>Choice</b> (logística consolidada) o no</td><td><span class="pill est">estimación</span></td></tr>
    <tr><td>PVP y Margen</td><td>Múltiplo que asigno según el tipo de producto</td><td><span class="pill est">estimación</span></td></tr>
    <tr><td>Competencia</td><td>Saturación de listados + qué tan fácil es conseguirlo en tienda física</td><td><span class="pill est">estimación</span></td></tr>
    <tr><td>Nota</td><td>Combinación ponderada de todo lo anterior</td><td><span class="pill est">estimación</span></td></tr>
  </table>
  <p><b>El PVP es una hipótesis, no una promesa.</b> Dice a cuánto <i>se podría</i> vender por tipo
  de producto, no a cuánto se vende hoy en tu mercado. Antes de comprar volumen, validá el precio real
  con la competencia que ya lo esté vendiendo en tu país.</p>
  <p><b>Costes que no están acá:</b> el coste es sólo el producto. Faltan envío al cliente,
  comisión de pasarela, impuestos y publicidad. En dropshipping la publicidad suele comerse
  la mitad del margen bruto, así que un 70% en la tabla no es un 70% en tu bolsillo.</p>
  <p id="fx"></p>
</footer>

<script>
const P = __DATOS__, M = __META__;
const $ = s => document.querySelector(s);
const money = n => '$' + n.toFixed(2);
const nSold = n => n >= 1000 ? (n/1000).toFixed(n>=10000?0:1).replace('.0','') + 'k' : n;

document.getElementById('crudo').textContent = M.total_crudo.toLocaleString('es');
document.getElementById('fecha').textContent = 'generado el ' + M.generado;
$('#fx').innerHTML = 'Los precios del catálogo venían en pesos argentinos. Convertidos a dólar a '
  + '<b>' + M.rate_ars.toLocaleString('es') + ' ARS/USD</b>, tipo de cambio deducido de productos '
  + 'capturados en las dos monedas. Si el dólar se movió mucho, los costes se corren en bloque.';

const avg = f => P.reduce((a,b)=>a+f(b),0)/P.length;
$('#k1').textContent = M.total_filtrado;
$('#k2').textContent = money(avg(p=>p.coste));
$('#k3').textContent = Math.round(avg(p=>p.margen_pct)) + '%';
$('#k4').textContent = avg(p=>p.multiplo).toFixed(1) + 'x';
$('#k5').textContent = P.filter(p=>p.competencia==='Baja').length + '/50';
$('#k6').textContent = P.filter(p=>p.choice).length + '/50';

[...new Set(P.map(p=>p.nicho))].sort().forEach(n=>{
  const o=document.createElement('option'); o.textContent=n; $('#fn').appendChild(o);
});

let sortK='score', sortD=-1;
const cls = s => s>=75?'s-a':s>=68?'s-b':'s-c';

function vista(){
  const q=$('#q').value.toLowerCase().trim(), fn=$('#fn').value,
        fc=$('#fc').value, fe=$('#fe').value, fp=$('#fp').value;
  let r = P.filter(p=>{
    if(q && !(p.titulo+' '+p.nicho+' '+p.categoria).toLowerCase().includes(q)) return false;
    if(fn && p.nicho!==fn) return false;
    if(fc && p.competencia!==fc) return false;
    if(fe==='fast' && !p.choice) return false;
    if(fe==='slow' && p.choice) return false;
    if(fp){const[a,b]=fp.split('-').map(Number); if(p.coste<a||p.coste>=b) return false;}
    return true;
  });
  r.sort((a,b)=>{
    let x=a[sortK], y=b[sortK];
    if(sortK==='competencia'){const o={Baja:0,Media:1,Alta:2}; x=o[x]; y=o[y];}
    if(sortK==='envio'){x=a.choice?0:1; y=b.choice?0:1;}
    if(typeof x==='string') return sortD*x.localeCompare(y);
    return sortD*((x??0)-(y??0));
  });
  return r;
}

function pinta(){
  const r=vista(), tb=$('#tb'); tb.innerHTML='';
  $('#cnt').textContent = r.length + ' de ' + P.length;
  $('#empty').style.display = r.length ? 'none' : 'block';
  r.forEach(p=>{
    const i = P.indexOf(p)+1;
    const tr=document.createElement('tr');
    tr.innerHTML =
      '<td class="rank">'+i+'</td>'+
      '<td><img class="th" loading="lazy" src="'+p.imagen+'" alt=""></td>'+
      '<td class="tt"><a href="'+p.url+'" target="_blank" rel="noopener">'+p.titulo+'</a>'+
        '<div class="cat">'+p.categoria+'</div></td>'+
      '<td><span class="tag n-'+p.nicho.replace(/ /g,'-')+'">'+p.nicho+'</span></td>'+
      '<td class="num">'+money(p.coste)+'</td>'+
      '<td class="num">'+money(p.pvp_sugerido)+'<div class="mult">'+p.multiplo+'x</div></td>'+
      '<td class="num">'+money(p.margen_usd)+'<div class="mult">'+p.margen_pct+'%</div></td>'+
      '<td class="num">'+nSold(p.vendidos)+'</td>'+
      '<td class="num">'+(p.rating??'–')+'</td>'+
      '<td class="c-'+p.competencia+'">'+p.competencia+'</td>'+
      '<td class="'+(p.choice?'fast':'slow')+'">'+p.envio+'</td>'+
      '<td class="num"><span class="score '+cls(p.score)+'">'+p.score+'</span></td>';
    const dt=document.createElement('tr'); dt.className='det';
    dt.innerHTML='<td colspan="12"><div class="det-in">'+detalle(p)+'</div></td>';
    tr.onclick=e=>{ if(e.target.tagName==='A') return;
      dt.querySelector('.det-in').classList.toggle('open'); };
    tb.appendChild(tr); tb.appendChild(dt);
  });
}

function detalle(p){
  const dias = p.dias_publicado==null ? '–' : p.dias_publicado + ' días';
  let w = '';
  if(p.riesgo_regulatorio) w='<div class="warn-box">⚠ Hace una afirmación médica o estética '+
    'regulada. Meta y Google suelen rechazar estos anuncios y puede exigir permisos sanitarios. '+
    'Revisalo antes de invertir en publicidad.</div>';
  return w+
  '<div class="grid">'+
    f('Coste unitario', money(p.coste)) +
    f('PVP sugerido', money(p.pvp_sugerido) + ' <span class="mult">('+p.multiplo+'x)</span>') +
    f('Margen bruto', money(p.margen_usd) + ' <span class="mult">('+p.margen_pct+'%)</span>') +
    f('Unidades vendidas', p.vendidos.toLocaleString('es')) +
    f('Valoración', (p.rating??'–') + ' ★') +
    f('Competidores', p.competidores + ' listados') +
    f('Envío', p.envio + (p.choice?' <span class="mult">(Choice)</span>':'')) +
    f('Publicado hace', dias) +
    f('Nota final', p.score) +
  '</div>'+
  '<div class="note"><b>Por qué está en la lista:</b> ' + porque(p) + '</div>'+
  '<a class="btn" href="'+p.url+'" target="_blank" rel="noopener">Ver en el proveedor →</a>';
}
const f=(k,v)=>'<div class="f"><span>'+k+'</span><b>'+v+'</b></div>';

function porque(p){
  const s=[];
  s.push(p.vendidos>=5000 ? 'Demanda ya probada, con '+p.vendidos.toLocaleString('es')+' unidades vendidas'
       : p.vendidos>=1000 ? 'Ventas sostenidas ('+p.vendidos.toLocaleString('es')+' unidades)'
       : 'Tracción inicial real ('+p.vendidos.toLocaleString('es')+' unidades)');
  s.push(p.multiplo>=3.8 ? 'es un aparato, no un accesorio, así que aguanta un margen de '+p.multiplo+'x'
       : 'admite alrededor de '+p.multiplo+'x sobre el coste');
  if(p.retail_fisico<=0.2) s.push('es difícil de conseguir en una tienda física, que es lo que te deja fijar el precio');
  else if(p.retail_fisico<=0.4) s.push('se consigue poco en tienda física');
  else s.push('ojo: algo parecido se consigue en tienda física, así que competís contra ese precio');
  s.push(p.competencia==='Baja' ? 'y el nicho todavía no está saturado'
       : p.competencia==='Media' ? 'y la competencia es manejable' : 'aunque la competencia es alta');
  if(p.choice) s.push('Además entra por logística Choice, que llega bastante más rápido');
  return s.join(', ').replace(/, ([^,]*)$/, ', $1') + '.';
}

document.querySelectorAll('th[data-k]').forEach(th=>{
  th.onclick=()=>{
    const k=th.dataset.k;
    if(sortK===k) sortD*=-1; else {sortK=k; sortD=(k==='titulo'||k==='nicho')?1:-1;}
    document.querySelectorAll('th .ar').forEach(a=>a.textContent='');
    th.querySelector('.ar').textContent = sortD===-1?'▼':'▲';
    pinta();
  };
});
['#q','#fn','#fc','#fe','#fp'].forEach(s=>{
  $(s).addEventListener(s==='#q'?'input':'change',pinta);
});
$('#rs').onclick=()=>{['#q','#fn','#fc','#fe','#fp'].forEach(s=>$(s).value=''); pinta();};
pinta();
</script>
</body></html>
"""

out = HTML.replace("__DATOS__", datos).replace("__META__", meta)
path = os.path.join(BASE, "dashboard.html")
open(path, "w", encoding="utf-8").write(out)
print("dashboard.html escrito:", len(out), "bytes,", len(P), "productos")
