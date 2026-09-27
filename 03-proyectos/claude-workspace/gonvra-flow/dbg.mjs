import { abrir, cerrarOverlays } from './lote.mjs';
const { browser, page } = await abrir();
await cerrarOverlays(page);
const botones = page.locator('button:has-text("add")');
console.log('botones add:', await botones.count());
await botones.last().click(); await page.waitForTimeout(3000);
const items = await page.evaluate(()=>{
  const vis=(el)=>{const r=el.getBoundingClientRect();return r.width>20&&r.height>14;};
  const o=[]; document.querySelectorAll('*').forEach(e=>{
    if(!vis(e)) return;
    const t=(e.textContent||'').trim();
    if(t && t.length>4 && t.length<45 && e.children.length===0) o.push(t);
  });
  return [...new Set(o)].slice(0,25);
});
console.log('MENÚ:\n  ' + items.join('\n  '));
console.log('inputs file:', await page.locator('input[type=file]').count());
await browser.close();
