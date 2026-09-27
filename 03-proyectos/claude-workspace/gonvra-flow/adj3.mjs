import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront(); await page.waitForTimeout(1500);

const abierto = await page.evaluate(()=>!!document.querySelector('.cdk-overlay-backdrop-showing'));
if (!abierto) { await page.locator('button:has-text("add")').last().click(); await page.waitForTimeout(2500); }

// clic en la tarjeta que contiene ese nombre
const ok = await page.evaluate(() => {
  const spans = [...document.querySelectorAll('span,div')].filter(e => (e.textContent||'').trim() === 'ref-3-uso-brazo.jpg');
  if (!spans.length) return 'no-encontrado';
  let el = spans[0];
  for (let i = 0; i < 8 && el; i++) {
    const r = el.getBoundingClientRect();
    if (r.width > 60 && r.height > 60) {
      el.scrollIntoView({ block: 'center' });
      el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));
      return `click en <${el.tagName} class="${(el.className||'').toString().slice(0,50)}"> ${Math.round(r.width)}x${Math.round(r.height)}`;
    }
    el = el.parentElement;
  }
  return 'sin contenedor clickeable';
});
console.log('→', ok);
await page.waitForTimeout(2500);

const add = page.getByText('Añadir a petición').first();
if (await add.count() && await add.isVisible().catch(()=>false)) { await add.click(); console.log('✓ añadido'); }
else { console.log('botón "Añadir a petición" no disponible'); }
await page.waitForTimeout(4000);
await page.screenshot({path:'/tmp/f5.png',timeout:60000,animations:'disabled',clip:{x:0,y:420,width:1440,height:480}}).catch(()=>{});
await browser.close();
