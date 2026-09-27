import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com'));
await page.bringToFront();
// volver al proyecto
await page.goBack().catch(()=>{});
await page.waitForTimeout(6000);
console.log('URL →', page.url());

const abierto = await page.evaluate(()=>!!document.querySelector('.cdk-overlay-backdrop-showing'));
if (!abierto) { await page.locator('button:has-text("add")').last().click(); await page.waitForTimeout(3000); }

// hover sobre la tarjeta y buscar el botón "Añadir a petición" dentro de ella
const res = await page.evaluate(() => {
  const spans=[...document.querySelectorAll('span')].filter(e=>(e.textContent||'').trim()==='ref-3-uso-brazo.jpg');
  if(!spans.length) return 'no está el archivo';
  let tile=spans[0];
  for(let i=0;i<10 && tile;i++){ if(/TILE|CARD/i.test(tile.tagName)&&tile.getBoundingClientRect().width>100) break; tile=tile.parentElement; }
  if(!tile) return 'sin tile';
  tile.dispatchEvent(new MouseEvent('mouseover',{bubbles:true}));
  tile.dispatchEvent(new MouseEvent('mouseenter',{bubbles:true}));
  const botones=[...tile.querySelectorAll('button,[role=button]')].map(b=>(b.innerText||b.getAttribute('aria-label')||'').trim());
  return 'tile=' + tile.tagName + ' botones=' + JSON.stringify(botones);
});
console.log('→', res);
await page.waitForTimeout(1500);

const add = page.getByRole('button', { name: /Añadir a petición/i }).first();
const cnt = await add.count();
console.log('botones "Añadir a petición":', cnt);
if (cnt) { await add.click({ force: true }); console.log('✓ añadido a la petición'); }
await page.waitForTimeout(4000);
await page.screenshot({path:'/tmp/f6.png',timeout:60000,animations:'disabled',clip:{x:0,y:420,width:1440,height:480}}).catch(()=>{});
await browser.close();
