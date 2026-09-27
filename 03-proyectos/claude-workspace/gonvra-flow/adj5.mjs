import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com'));
await page.bringToFront();
await page.goto('https://flow.google.com/project/a6872b5e-edc6-4445-8616-7e517d274404', { waitUntil:'domcontentloaded', timeout:60000 });
await page.waitForTimeout(9000);

await page.locator('button:has-text("add")').last().click();
await page.waitForTimeout(3500);

// hover real con el mouse sobre la tarjeta
const caja = await page.evaluate(() => {
  const spans=[...document.querySelectorAll('span')].filter(e=>(e.textContent||'').trim()==='ref-3-uso-brazo.jpg');
  if(!spans.length) return null;
  let el=spans[0];
  for(let i=0;i<10&&el;i++){ const r=el.getBoundingClientRect(); if(r.width>120&&r.height>120) return {x:r.x+r.width/2,y:r.y+r.height/2,w:r.width,h:r.height,tag:el.tagName}; el=el.parentElement; }
  return null;
});
console.log('tarjeta →', JSON.stringify(caja));
if (caja) {
  await page.mouse.move(caja.x, caja.y);
  await page.waitForTimeout(2000);
  const bots = await page.evaluate(()=>[...document.querySelectorAll('button,[role=button]')]
    .filter(b=>{const r=b.getBoundingClientRect();return r.width>10&&r.height>10;})
    .map(b=>(b.innerText||b.getAttribute('aria-label')||'').trim()).filter(t=>t&&t.length<40));
  console.log('visibles al hover:', [...new Set(bots)].slice(-12).join(' | '));
  const add = page.getByRole('button',{name:/Añadir a petición/i}).first();
  if (await add.count()) { await add.click({force:true}); console.log('✓ AÑADIDO'); }
  else {
    const alt = page.locator('[aria-label*="Añadir"], button:has-text("Añadir")').first();
    if (await alt.count()) { await alt.click({force:true}); console.log('✓ añadido (alt)'); }
    else console.log('✗ no encontré el botón');
  }
}
await page.waitForTimeout(4000);
await page.screenshot({path:'/tmp/f7.png',timeout:60000,animations:'disabled',clip:{x:0,y:420,width:1440,height:480}}).catch(()=>{});
await browser.close();
