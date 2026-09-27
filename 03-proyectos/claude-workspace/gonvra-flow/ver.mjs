import { abrir, cerrarOverlays } from './lote.mjs';
const { browser, page } = await abrir();
await cerrarOverlays(page);
await page.waitForTimeout(1500);
console.log('URL →', page.url());
const s = await page.evaluate(()=>{
  const vis=(el)=>{const r=el.getBoundingClientRect();return r.width>20&&r.height>14;};
  const b=[]; document.querySelectorAll('button,[role=button]').forEach(x=>{ if(!vis(x))return;
    const t=(x.innerText||x.getAttribute('aria-label')||'').trim().replace(/\s+/g,' ');
    if(t&&t.length>2&&!/play_circle|^\d+p$/.test(t)) b.push(t.slice(0,44));});
  return [...new Set(b)];
});
console.log('BOTONES:', s.join(' | '));
await browser.close();
