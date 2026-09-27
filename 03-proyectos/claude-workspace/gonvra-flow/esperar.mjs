import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com/project'));
await page.bringToFront();
for (let i = 0; i < 20; i++) {
  await page.waitForTimeout(15000);
  const est = await page.evaluate(() => {
    const t = document.body.innerText;
    const gen = /gener|creando|procesando|loading/i.test(t);
    const vids = document.querySelectorAll('video').length;
    return { gen, vids, muestra: t.slice(0, 120).replace(/\s+/g,' ') };
  });
  console.log(`[${(i+1)*15}s] generando=${est.gen}  videos=${est.vids}`);
  if (!est.gen && i > 2) break;
}
await page.screenshot({path:'/tmp/f9.png',timeout:60000,animations:'disabled',clip:{x:260,y:0,width:1180,height:560}}).catch(()=>{});
await browser.close();
