import { abrir } from './lote.mjs';
const { browser, page } = await abrir();
await page.waitForTimeout(1500);
const info = await page.evaluate(()=>{
  const el=[...document.querySelectorAll('*')].find(e=>e.children.length===0 && (e.textContent||'').trim()==='Subir archivo multimedia');
  if(!el) return {hay:false};
  let p=el, cadena=[];
  for(let i=0;i<5&&p;i++){ cadena.push(`${p.tagName}${p.className?'.'+String(p.className).split(' ')[0]:''}`); p=p.parentElement; }
  const clickable = el.closest('button,[role=button],label,a');
  const r=el.getBoundingClientRect();
  return { hay:true, cadena, clickable: clickable?clickable.tagName+(clickable.getAttribute('for')?`[for=${clickable.getAttribute('for')}]`:''):null,
           pos:{x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width)}, inputs: document.querySelectorAll('input[type=file]').length };
});
console.log(JSON.stringify(info,null,1));
await browser.close();
