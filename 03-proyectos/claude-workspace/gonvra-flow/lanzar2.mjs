import { chromium } from 'playwright-core';
const PROMPT='Animate this exact photograph with minimal motion. The hand slides the shaver down the forearm ONE single slow continuous stroke, revealing a clean trimmed strip behind it. The camera stays almost completely still. CRITICAL: the device must stay rigid and geometrically identical to the reference image in every frame, same silhouette, same proportions, same lime-green button, same wide steel head. Do not bend, stretch or redesign it. No logos, no text. Natural window light, realistic skin texture, photorealistic.';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com/project'));
await page.bringToFront(); await page.waitForTimeout(1500);

// enfocar el contenteditable directamente
const ok = await page.evaluate(()=>{
  const ed=[...document.querySelectorAll('[contenteditable=true]')].filter(e=>e.getBoundingClientRect().width>200);
  if(!ed.length) return 'sin editor';
  ed[0].focus();
  const r=ed[0].getBoundingClientRect();
  return `editor ${Math.round(r.width)}x${Math.round(r.height)} en y=${Math.round(r.y)}`;
});
console.log('→', ok);
await page.waitForTimeout(600);
await page.keyboard.type(PROMPT, { delay: 3 });
await page.waitForTimeout(2500);
const chars = await page.evaluate(()=>[...document.querySelectorAll('[contenteditable=true]')].map(e=>e.innerText).join('').length);
console.log('caracteres:', chars);

const flecha = page.locator('button:has-text("arrow_forward")').last();
await flecha.click({ timeout: 20000, force: true });
console.log('✓ GENERACIÓN LANZADA');
await page.waitForTimeout(25000);
await page.screenshot({path:'/tmp/f8.png',timeout:60000,animations:'disabled',clip:{x:0,y:260,width:1440,height:640}}).catch(()=>{});
await browser.close();
