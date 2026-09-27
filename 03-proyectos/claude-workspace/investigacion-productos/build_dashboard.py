#!/usr/bin/env python3
"""Genera dashboard.html interactivo desde products.json."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "products.json")
OUT = os.path.join(BASE, "dashboard.html")

TPL = r"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Investigacion de productos - Salud, belleza y cuidado personal</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0d0f13;color:#e6e8ee;font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif;padding:28px}
.wrap{max-width:1500px;margin:0 auto}
h1{font-size:24px;font-weight:650;letter-spacing:-.3px}
.sub{color:#8b93a7;margin-top:6px;font-size:13px}
.banner{margin:18px 0;padding:14px 16px;border-radius:10px;font-size:13px;line-height:1.6}
.warn{background:#2a1f0e;border:1px solid #5c4415;color:#f0c674}
.info{background:#0f1c2a;border:1px solid #1d3a57;color:#8fc4f0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:18px 0}
.kpi{background:#141821;border:1px solid #222836;border-radius:10px;padding:14px}
.kpi .n{font-size:22px;font-weight:650}
.kpi .l{color:#8b93a7;font-size:11px;text-transform:uppercase;letter-spacing:.6px;margin-top:3px}
.panel{background:#141821;border:1px solid #222836;border-radius:10px;padding:16px;margin-bottom:16px}
.panel h3{font-size:12px;text-transform:uppercase;letter-spacing:.7px;color:#8b93a7;margin-bottom:12px}
.row{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end}
.f{display:flex;flex-direction:column;gap:5px}
.f label{font-size:11px;color:#8b93a7}
input,select{background:#0d0f13;border:1px solid #2a3142;color:#e6e8ee;padding:7px 10px;border-radius:7px;font-size:13px;outline:none}
input:focus,select:focus{border-color:#3b82f6}
input[type=number]{width:82px}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;padding:10px 8px;color:#8b93a7;font-size:11px;text-transform:uppercase;letter-spacing:.5px;border-bottom:1px solid #222836;cursor:pointer;white-space:nowrap;user-select:none}
th:hover{color:#e6e8ee}
td{padding:11px 8px;border-bottom:1px solid #1a1f2b;vertical-align:middle}
tr.p:hover{background:#171c26}
img.th{width:46px;height:46px;object-fit:cover;border-radius:7px;background:#222836;display:block}
.tt{font-weight:500;line-height:1.35;max-width:330px}
.tt a{color:#e6e8ee;text-decoration:none}
.tt a:hover{color:#60a5fa;text-decoration:underline}
.tag{display:inline-block;padding:2px 7px;border-radius:5px;font-size:11px;font-weight:500;white-space:nowrap}
.t-disp{background:#12331f;color:#5ddc8f}.t-herr{background:#1a2740;color:#7dabf0}.t-cons{background:#33241a;color:#e0a06a}
.c-Baja{background:#12331f;color:#5ddc8f}.c-Media{background:#33301a;color:#ddc76a}.c-Alta{background:#331a1a;color:#e07a7a}
.sc{font-weight:650;font-size:15px}
.money{font-variant-numeric:tabular-nums;white-space:nowrap}
.pos{color:#5ddc8f}
.mut{color:#8b93a7;font-size:12px}
.flag{color:#e0a06a;font-size:11px}
.nota{background:#10141c;border-left:2px solid #3b82f6;padding:10px 13px;color:#b9c0d0;font-size:12.5px;line-height:1.6}
.est{border-bottom:1px dotted #5c6478;cursor:help}
.legend{display:flex;gap:20px;flex-wrap:wrap;font-size:12px;color:#8b93a7}
.legend b{color:#e6e8ee}
button{background:#1e2534;border:1px solid #2a3142;color:#e6e8ee;padding:8px 14px;border-radius:7px;cursor:pointer;font-size:13px}
button:hover{background:#26304a}
.empty{padding:44px;text-align:center;color:#8b93a7}
</style></head><body><div class="wrap">

<h1>Productos ganadores - Salud, belleza y cuidado personal</h1>
<div class="sub" id="sub"></div>

<div id="banner"></div>

<div class="cards" id="kpis"></div>

<div class="panel">
  <h3>Filtros</h3>
  <div class="row">
    <div class="f"><label>Buscar</label><input id="q" placeholder="palabra clave..." style="width:200px"></div>
    <div class="f"><label>Nicho</label><select id="fn"></select></div>
    <div class="f"><label>Tipo</label><select id="ft"></select></div>
    <div class="f"><label>Competencia</label><select id="fc"></select></div>
    <div class="f"><label>Coste min US$</label><input type="number" id="cmin" value="5" step="1"></div>
    <div class="f"><label>Coste max US$</label><input type="number" id="cmax" value="30" step="1"></div>
    <div class="f"><label>Ventas min</label><input type="number" id="vmin" value="0" step="50"></div>
    <div class="f"><label>&nbsp;</label><button id="reset">Limpiar</button></div>
    <div class="f"><label>&nbsp;</label><button id="csv">Exportar CSV</button></div>
  </div>
</div>

<div class="panel">
  <h3>Supuesto de precio de venta &mdash; edítalo y el margen se recalcula</h3>
  <div class="row">
    <div class="f"><label>Dispositivo (x)</label><input type="number" id="m_disp" step="0.1" min="1"></div>
    <div class="f"><label>Herramienta (x)</label><input type="number" id="m_herr" step="0.1" min="1"></div>
    <div class="f"><label>Consumible (x)</label><input type="number" id="m_cons" step="0.1" min="1"></div>
    <div class="f" style="flex:1;min-width:280px"><label>&nbsp;</label>
      <div class="mut">El multiplicador es un <b>supuesto mío</b>, no un dato del proveedor. Cambialo y mirá cómo se mueve el margen.</div>
    </div>
  </div>
</div>

<div class="panel" style="padding:0;overflow-x:auto">
  <table id="tb"><thead><tr>
    <th data-k="rank">#</th><th></th>
    <th data-k="titulo">Producto</th>
    <th data-k="nicho">Nicho</th>
    <th data-k="tipo">Tipo</th>
    <th data-k="coste">Coste</th>
    <th data-k="pvp_sugerido">PVP sug.</th>
    <th data-k="margen_usd">Margen</th>
    <th data-k="margen_pct">%</th>
    <th data-k="vendidos">Ventas</th>
    <th data-k="rating">Rating</th>
    <th data-k="competidores">Competencia</th>
    <th data-k="envio">Envío</th>
    <th data-k="score">Nota</th>
  </tr></thead><tbody id="tbody"></tbody></table>
  <div class="empty" id="empty" style="display:none">Ningún producto cumple estos filtros.</div>
</div>

<div class="panel">
  <h3>De dónde sale cada dato</h3>
  <div class="legend">
    <div><b>DATO real:</b> coste, ventas, rating, descuento, Choice, envío gratis</div>
    <div><b>MODELO (supuesto mío):</b> PVP, margen, competencia, nicho, tipo, nota final</div>
    <div><b>No disponible:</b> días exactos de envío</div>
  </div>
  <div class="mut" style="margin-top:12px" id="prov"></div>
</div>

<script>
const D = __DATA__;
const P = D.productos.map((p,i)=>({...p, rank:i+1}));
const $ = s=>document.querySelector(s);
const fmt = n => n.toLocaleString('es-AR',{minimumFractionDigits:2,maximumFractionDigits:2});
const fint = n => n.toLocaleString('es-AR');
let sortK='score', sortD=-1, current=[];

$('#sub').textContent = `Fuente: ${D.fuente} · ${fint(D.total_crudo)} productos crudos analizados · `
  + `${D.total_filtrado} pasaron los 5 criterios · generado ${D.generado}`;

// banner honesto sobre cobertura
const b=[];
if(D.entregados < 50){
  b.push(`<div class="banner warn"><b>Atención: hay ${D.entregados} productos, no 50.</b><br>
  Solo se pudieron relevar ${fint(D.total_crudo)} productos crudos del catálogo antes de que el proveedor
  cortara el acceso automático por volumen de consultas. De esos, ${D.total_filtrado} cumplen tus 5 criterios.
  El resto se completa cuando entre más catálogo (el recolector sigue corriendo en segundo plano)
  o cuando cargues la exportación CSV de AutoDS. <b>No se rellenó con productos inventados a propósito.</b></div>`);
}
b.push(`<div class="banner info"><b>Cómo leer esto.</b> El coste, las ventas y el rating son datos reales del catálogo.
El precio de venta y el margen son un <b>supuesto</b> que podés editar arriba. La competencia se mide contando
cuántos listados de la misma categoría ya tienen ventas probadas dentro de lo relevado &mdash; es un indicador
relativo, no la cuota de mercado real.</div>`);
$('#banner').innerHTML = b.join('');

const dsc = Object.entries(D.descartes||{}).map(([k,v])=>`${k}: ${v}`).join(' · ');
$('#prov').innerHTML = `Descartes al aplicar los criterios &rarr; ${dsc||'ninguno'}. `
  + `Tipo de cambio usado: 1 USD = ${fmt(D.fx_usd_ars)} ARS.`;

// KPIs
function kpis(rows){
  const n=rows.length;
  const mm=n?rows.reduce((a,x)=>a+x.margen_usd,0)/n:0;
  const mc=n?rows.reduce((a,x)=>a+x.coste,0)/n:0;
  const mv=n?rows.reduce((a,x)=>a+x.vendidos,0)/n:0;
  const nb=rows.filter(x=>x.competencia==='Baja').length;
  $('#kpis').innerHTML=[
    ['Productos',fint(n)],['Margen medio','US$ '+fmt(mm)],['Coste medio','US$ '+fmt(mc)],
    ['Ventas medias',fint(Math.round(mv))],['Competencia baja',fint(nb)]
  ].map(([l,v])=>`<div class="kpi"><div class="n">${v}</div><div class="l">${l}</div></div>`).join('');
}

// selects
function fill(sel,vals,lbl){
  sel.innerHTML=`<option value="">${lbl}</option>`+vals.map(v=>`<option>${v}</option>`).join('');
}
fill($('#fn'),[...new Set(P.map(p=>p.nicho))].sort(),'Todos');
fill($('#ft'),[...new Set(P.map(p=>p.tipo))].sort(),'Todos');
fill($('#fc'),['Baja','Media','Alta'],'Todas');

const MK=D.markup_supuesto||{dispositivo:3.6,herramienta:3.0,consumible:2.5};
$('#m_disp').value=MK.dispositivo; $('#m_herr').value=MK.herramienta; $('#m_cons').value=MK.consumible;

function markup(t){
  if(t==='dispositivo')return +$('#m_disp').value||1;
  if(t==='consumible')return +$('#m_cons').value||1;
  return +$('#m_herr').value||1;
}

function apply(){
  // recalcular PVP/margen con el supuesto vivo
  P.forEach(p=>{
    const m=markup(p.tipo);
    p.markup=m; p.pvp_sugerido=+(p.coste*m).toFixed(2);
    p.margen_usd=+(p.pvp_sugerido-p.coste).toFixed(2);
    p.margen_pct=p.pvp_sugerido?+((p.margen_usd/p.pvp_sugerido)*100).toFixed(1):0;
  });
  const q=$('#q').value.toLowerCase(), fn=$('#fn').value, ft=$('#ft').value, fc=$('#fc').value;
  const cmin=+$('#cmin').value, cmax=+$('#cmax').value, vmin=+$('#vmin').value;
  let rows=P.filter(p=>
    (!q || p.titulo.toLowerCase().includes(q) || (p.nota||'').toLowerCase().includes(q)) &&
    (!fn || p.nicho===fn) && (!ft || p.tipo===ft) && (!fc || p.competencia===fc) &&
    p.coste>=cmin && p.coste<=cmax && p.vendidos>=vmin);
  rows.sort((a,b)=>{
    let x=a[sortK],y=b[sortK];
    if(typeof x==='string')return sortD*x.localeCompare(y);
    return sortD*((x??0)-(y??0));
  });
  current=rows; render(rows); kpis(rows);
}

function render(rows){
  $('#empty').style.display=rows.length?'none':'block';
  const tcls={dispositivo:'t-disp',herramienta:'t-herr',consumible:'t-cons'};
  $('#tbody').innerHTML=rows.map(p=>{
    const img=p.imagen?(p.imagen.startsWith('//')?'https:'+p.imagen:p.imagen):'';
    const flags=[p.commodity?'<span class="flag">se consigue en tienda física</span>':'',
                 p.voluminoso?'<span class="flag">voluminoso</span>':''].filter(Boolean).join(' · ');
    return `<tr class="p">
      <td class="mut">${p.rank}</td>
      <td>${img?`<img class="th" src="${img}" loading="lazy">`:''}</td>
      <td class="tt"><a href="${p.url}" target="_blank" rel="noopener">${p.titulo}</a>
        ${flags?`<div>${flags}</div>`:''}</td>
      <td class="mut">${p.nicho}</td>
      <td><span class="tag ${tcls[p.tipo]}">${p.tipo}</span></td>
      <td class="money">US$ ${fmt(p.coste)}${p.coste_exacto?'':' <span class="est" title="convertido desde ARS">~</span>'}</td>
      <td class="money est" title="supuesto: ${p.markup}x el coste">US$ ${fmt(p.pvp_sugerido)}</td>
      <td class="money pos">US$ ${fmt(p.margen_usd)}</td>
      <td class="money">${p.margen_pct}%</td>
      <td class="money">${fint(p.vendidos)}</td>
      <td class="money">${p.rating!=null?p.rating+'★':'<span class="mut">s/d</span>'}</td>
      <td><span class="tag c-${p.competencia}">${p.competencia}</span> <span class="mut">${p.competidores}</span></td>
      <td class="mut">${p.envio}</td>
      <td class="sc">${p.score}</td>
    </tr>
    <tr><td></td><td></td><td colspan="12" style="padding-top:0"><div class="nota">${p.nota}</div></td></tr>`;
  }).join('');
}

document.querySelectorAll('th[data-k]').forEach(th=>th.onclick=()=>{
  const k=th.dataset.k; sortD = (sortK===k)? -sortD : -1; sortK=k; apply();
});
['q','fn','ft','fc','cmin','cmax','vmin','m_disp','m_herr','m_cons']
  .forEach(id=>{const e=$('#'+id); e.oninput=apply; e.onchange=apply;});
$('#reset').onclick=()=>{$('#q').value='';$('#fn').value='';$('#ft').value='';$('#fc').value='';
  $('#cmin').value=5;$('#cmax').value=30;$('#vmin').value=0;apply();};
$('#csv').onclick=()=>{
  const cols=['rank','titulo','nicho','tipo','coste','pvp_sugerido','margen_usd','margen_pct',
              'vendidos','rating','competencia','envio','score','nota','url'];
  const data=current;
  const csv=[cols.join(',')].concat(data.map(p=>cols.map(c=>{
    const v=p[c]==null?'':String(p[c]).replace(/"/g,'""'); return `"${v}"`;}).join(','))).join('\n');
  const a=document.createElement('a');
  a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));
  a.download='productos-ganadores.csv'; a.click();
};
apply();
</script></div></body></html>
"""


def main():
    d = json.load(open(DATA, encoding="utf-8"))
    html = TPL.replace("__DATA__", json.dumps(d, ensure_ascii=False))
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"dashboard -> {OUT} | productos: {len(d['productos'])}")


if __name__ == "__main__":
    main()
