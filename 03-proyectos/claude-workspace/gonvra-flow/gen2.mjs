import { chromium } from 'playwright-core';
const REF='/home/matiigonzz/Claude/gonvra-brand/flow-refs/ref-3-uso-brazo.jpg';
const PROMPT='Animate this exact photograph with minimal motion. The hand slides the shaver down the forearm ONE single slow continuous stroke, revealing a clean trimmed strip behind it. The camera stays almost completely still. CRITICAL: the device must stay rigid and geometrically identical to the reference image in every frame, same silhouette, same proportions, same lime-green button, same wide steel head. Do not bend, stretch or redesign it. No logos, no text. Natural window light, realistic skin texture, photorealistic.';

const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront(); await page.waitForTimeout(1500);

// 1) adjuntar
await page.locator('button:has-text("add")').last().click();
await page.waitForTimeout(2200);
const [fc] = await Promise.all([
  page.waitForEvent('filechooser', { timeout: 25000 }),
  page.getByText('Subir archivo multimedia').first().click(),
]);
await fc.setFiles(REF);
console.log('✓ archivo enviado');
await page.waitForTimeout(12000);

// cerrar cualquier overlay que quede
for (let i=0;i<3;i++){
  const hay = await page.evaluate(()=>!!document.querySelector('.cdk-overlay-backdrop-showing'));
  if(!hay) break;
  await page.keyboard.press('Escape'); await page.waitForTimeout(1200);
}

// 2) escribir la petición: clic sobre el placeholder
await page.getByText('¿Qué quieres crear?').first().click({ timeout: 12000 }).catch(()=>{});
await page.waitForTimeout(1000);
await page.keyboard.type(PROMPT, { delay: 3 });
await page.waitForTimeout(1500);

const escrito = await page.evaluate(()=>{
  const t=document.querySelector('textarea'); 
  const ce=[...document.querySelectorAll('[contenteditable=true]')].map(e=>e.innerText).join('');
  return { textarea:(t&&t.value||'').slice(0,80), editable: ce.slice(0,80) };
});
console.log('texto en textarea :', escrito.textarea);
console.log('texto en editable :', escrito.editable);
await page.screenshot({path:'/tmp/f3.png',timeout:60000,animations:'disabled',clip:{x:0,y:480,width:1440,height:420}}).catch(()=>{});
await browser.close();
