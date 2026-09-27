import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = ctx.pages().find(p => p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront(); await page.waitForTimeout(3000);
const inv = await page.evaluate(() => {
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 20 && r.height > 14; };
  const bot = [];
  document.querySelectorAll('button,[role=button],[role=combobox]').forEach((b) => {
    if (!vis(b)) return;
    const t = (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\s+/g,' ');
    if (t && t.length > 2 && !/^play_circle|^\d+p$/.test(t)) bot.push(t.slice(0,46));
  });
  const inp = [];
  document.querySelectorAll('textarea,input').forEach((i) => {
    inp.push(`${i.tagName}[${i.type||'-'}] ph="${(i.placeholder||'').slice(0,70)}" vis=${i.offsetParent!==null}`);
  });
  return { bot: [...new Set(bot)], inp };
});
console.log('BOTONES:\n  ' + inv.bot.join('\n  '));
console.log('\nINPUTS:\n  ' + inv.inp.join('\n  '));
await browser.close();
