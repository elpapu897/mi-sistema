import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = ctx.pages().find(p => p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront();
await page.keyboard.press('Escape'); await page.waitForTimeout(1500);
await page.keyboard.press('Escape'); await page.waitForTimeout(2500);
const s = await page.evaluate(() => {
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width>20 && r.height>14; };
  const b=[]; document.querySelectorAll('button,[role=button]').forEach(x=>{ if(!vis(x))return;
    const t=(x.innerText||x.getAttribute('aria-label')||'').trim().replace(/\s+/g,' ');
    if(t&&t.length>2&&!/play_circle|^\d+p$/.test(t)) b.push(t.slice(0,50));});
  return { botones:[...new Set(b)], overlay: !!document.querySelector('.cdk-overlay-backdrop-showing') };
});
console.log('overlay abierto:', s.overlay);
console.log('BOTONES:\n  ' + s.botones.join('\n  '));
await page.screenshot({ path:'/tmp/f2.png', timeout:60000, animations:'disabled', clip:{x:0,y:540,width:1440,height:360}}).catch(()=>console.log('sin captura'));
await browser.close();
