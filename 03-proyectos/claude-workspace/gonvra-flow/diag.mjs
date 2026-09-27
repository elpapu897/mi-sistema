import { abrir, cerrarOverlays } from './lote.mjs';
const { browser, page } = await abrir();
await cerrarOverlays(page); await page.waitForTimeout(2000);
const t = await page.evaluate(()=>{
  const i=[...document.querySelectorAll('img')].filter(x=>{const r=x.getBoundingClientRect();return r.width>140&&r.height>180&&r.x>200;})[0];
  if(!i) return null; const r=i.getBoundingClientRect();
  return {x:Math.round(r.x+r.width/2),y:Math.round(r.y+r.height/2),alt:i.alt||'',src:(i.src||'').slice(0,70)};
});
console.log('primera tarjeta:', JSON.stringify(t));
if (t) {
  await page.mouse.move(t.x, t.y); await page.waitForTimeout(2000);
  const hover = await page.evaluate(()=>[...document.querySelectorAll('button,[role=button]')]
    .filter(b=>{const r=b.getBoundingClientRect();return r.width>14&&r.height>14;})
    .map(b=>(b.innerText||b.getAttribute('aria-label')||'').trim()).filter(x=>x&&x.length<30));
  console.log('al pasar el mouse:', [...new Set(hover)].slice(-14).join(' | '));
}
await browser.close();
