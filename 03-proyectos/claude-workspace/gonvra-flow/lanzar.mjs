import { chromium } from 'playwright-core';
const PROMPT='Animate this exact photograph with minimal motion. The hand slides the shaver down the forearm ONE single slow continuous stroke, revealing a clean trimmed strip behind it. The camera stays almost completely still. CRITICAL: the device must stay rigid and geometrically identical to the reference image in every frame, same silhouette, same proportions, same lime-green button, same wide steel head. Do not bend, stretch or redesign it. No logos, no text. Natural window light, realistic skin texture, photorealistic.';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com/project'));
await page.bringToFront(); await page.waitForTimeout(1500);

await page.getByText('¿Qué quieres crear?').first().click({timeout:12000});
await page.waitForTimeout(800);
await page.keyboard.type(PROMPT, { delay: 3 });
await page.waitForTimeout(2000);

const listo = await page.evaluate(()=> [...document.querySelectorAll('[contenteditable=true]')].map(e=>e.innerText).join('').length);
console.log('caracteres escritos:', listo);

// generar
const flecha = page.locator('button:has-text("arrow_forward")').last();
console.log('botón generar:', await flecha.count());
await flecha.click({ timeout: 15000 });
console.log('✓ GENERANDO — esperando…');
await page.waitForTimeout(20000);
await page.screenshot({path:'/tmp/f8.png',timeout:60000,animations:'disabled',clip:{x:0,y:300,width:1440,height:600}}).catch(()=>{});
await browser.close();
