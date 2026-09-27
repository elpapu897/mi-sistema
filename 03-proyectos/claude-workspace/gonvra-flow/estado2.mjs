import { abrir } from './lote.mjs';
const { browser, page } = await abrir();
// cerrar el panel lateral de subidas
for (const t of ['Ocultar','close']) {
  const b = page.getByText(t).first();
  if (await b.count()) { await b.click().catch(()=>{}); await page.waitForTimeout(2000); }
}
await page.goto('https://flow.google.com/project/a6872b5e-edc6-4445-8616-7e517d274404', { waitUntil:'domcontentloaded' });
await page.waitForTimeout(10000);
const r = await page.evaluate(()=>{
  const txt = document.body.innerText;
  const prompts = [...document.querySelectorAll('*')].filter(e=>e.children.length===0)
    .map(e=>(e.textContent||'').trim())
    .filter(t=>/Animate this exact|Camera pushing|rotate|sliding|push-in/i.test(t)).slice(0,10);
  return { generando: /gener|creando|procesando/i.test(txt), videos: document.querySelectorAll('video').length, prompts };
});
console.log('generando:', r.generando, '| videos en DOM:', r.videos);
console.log('peticiones visibles:\n  ' + r.prompts.map(p=>p.slice(0,70)).join('\n  '));
await browser.close();
