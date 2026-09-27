import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront(); await page.waitForTimeout(1200);

await page.locator('button:has-text("add")').last().click();
await page.waitForTimeout(2500);

// listar los primeros items de la biblioteca
const items = await page.evaluate(()=>{
  const vis=(el)=>{const r=el.getBoundingClientRect();return r.width>30&&r.height>20;};
  const o=[];
  document.querySelectorAll('[role=menuitem],[role=option],li,button').forEach(b=>{
    if(!vis(b))return; const t=(b.innerText||'').trim().replace(/\s+/g,' ');
    if(t&&t.length>3&&t.length<70&&!/play_circle|^\d+p$|^add$|^help$/.test(t)) o.push(t);
  });
  return [...new Set(o)].slice(0,14);
});
console.log('BIBLIOTECA:\n  ' + items.join('\n  '));

// buscar el frame recién subido
const cand = page.getByText(/ref-3-uso-brazo/i).first();
if (await cand.count()) {
  await cand.click(); console.log('✓ seleccioné ref-3-uso-brazo');
} else {
  // si no aparece por nombre, tomar el primer elemento de imagen de la grilla
  console.log('no lo encontré por nombre');
}
await page.waitForTimeout(2000);
const add = page.getByText('Añadir a petición').first();
if (await add.count()) { await add.click(); console.log('✓ añadido a la petición'); }
await page.waitForTimeout(4000);
await page.screenshot({path:'/tmp/f4.png',timeout:60000,animations:'disabled',clip:{x:0,y:440,width:1440,height:460}}).catch(()=>{});
await browser.close();
