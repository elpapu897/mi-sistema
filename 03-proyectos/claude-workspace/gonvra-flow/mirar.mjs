import { abrir, cerrarOverlays } from './lote.mjs';
const { browser, page } = await abrir();
await cerrarOverlays(page); await page.waitForTimeout(2000);
// ocultar el panel lateral para ver la grilla
const oc = page.getByText('Ocultar').first();
if (await oc.count()) { await oc.click().catch(()=>{}); await page.waitForTimeout(2500); }
const info = await page.evaluate(()=>{
  const vids=[...document.querySelectorAll('video')].map(v=>{const r=v.getBoundingClientRect();return {x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),src:(v.currentSrc||v.src||'').slice(0,60)};});
  const imgs=[...document.querySelectorAll('img')].filter(i=>{const r=i.getBoundingClientRect();return r.width>140&&r.height>180&&r.x>200;})
    .map(i=>{const r=i.getBoundingClientRect();return {x:Math.round(r.x+r.width/2),y:Math.round(r.y+r.height/2),w:Math.round(r.width)};});
  return { vids: vids.length, imgs: imgs.length, primeras: imgs.slice(0,10) };
});
console.log(JSON.stringify(info,null,1).slice(0,900));
await browser.close();
