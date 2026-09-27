import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = ctx.pages().find(p => p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront();
await page.waitForTimeout(4000);
console.log('URL →', page.url());
const inv = await page.evaluate(() => {
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 4 && r.height > 4; };
  const out = { botones: [], inputs: [], texto: document.body.innerText.slice(0, 500) };
  document.querySelectorAll('button,[role=button],[role=combobox]').forEach((b) => {
    if (!vis(b)) return;
    const t = (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\s+/g,' ').slice(0,44);
    if (t) out.botones.push(t);
  });
  document.querySelectorAll('textarea,input').forEach((i) => {
    out.inputs.push(`${i.tagName}[${i.type||'-'}] ph="${(i.placeholder||'').slice(0,60)}"`);
  });
  return out;
});
console.log('BOTONES:', [...new Set(inv.botones)].join(' | '));
console.log('INPUTS :', inv.inputs.join(' | '));
console.log('--- TEXTO ---\n' + inv.texto);
await browser.close();
