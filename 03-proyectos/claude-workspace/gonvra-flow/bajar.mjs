import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = ctx.pages().find(p=>p.url().includes('flow.google.com'));
await page.bringToFront(); await page.waitForTimeout(2000);

// buscar la url del video directamente del DOM
const src = await page.evaluate(()=>{
  const v=document.querySelector('video');
  return v ? (v.currentSrc || v.src) : null;
});
console.log('src →', (src||'sin video').slice(0,120));

const [dl] = await Promise.all([
  page.waitForEvent('download', { timeout: 45000 }).catch(()=>null),
  page.locator('button:has-text("download"), [aria-label*="escarg"], [aria-label*="ownload"]').last().click({ timeout: 15000 }).catch(e=>console.log('click descarga falló')),
]);
if (dl) {
  const destino = '/home/matiigonzz/Descargas/GONVRA - flow/' + (dl.suggestedFilename() || 'flow-brazo.mp4');
  await dl.saveAs(destino);
  console.log('✓ DESCARGADO →', destino);
} else {
  console.log('no se disparó descarga; puede haber abierto un menú');
  const op = await page.evaluate(()=>[...document.querySelectorAll('[role=menuitem],button')]
    .filter(b=>{const r=b.getBoundingClientRect();return r.width>20&&r.height>14;})
    .map(b=>(b.innerText||'').trim()).filter(t=>t&&t.length<40));
  console.log('opciones:', [...new Set(op)].slice(-10).join(' | '));
}
await browser.close();
