import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = ctx.pages().find(p => p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront(); await page.waitForTimeout(2000);

// el "+" de la barra de petición
const mas = page.locator('button:has-text("add"), [role=button]:has-text("add")').last();
console.log('botones add:', await mas.count());
await mas.click({ timeout: 15000 });
await page.waitForTimeout(2500);

const menu = await page.evaluate(() => {
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 20 && r.height > 14; };
  const o = [];
  document.querySelectorAll('[role=menuitem],[role=option],button,li').forEach((b) => {
    if (!vis(b)) return;
    const t = (b.innerText||'').trim().replace(/\s+/g,' ');
    if (t && t.length > 2 && t.length < 60 && !/play_circle|^\d+p$/.test(t)) o.push(t);
  });
  return [...new Set(o)];
});
console.log('MENÚ:\n  ' + menu.join('\n  '));
console.log('file inputs:', await page.locator('input[type=file]').count());
await browser.close();
