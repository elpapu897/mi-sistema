import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const paginas = ctx.pages();
const page = paginas.find(p => p.url().includes('labs.google')) ?? paginas[paginas.length-1];
console.log('URL →', page.url());
const inv = await page.evaluate(() => {
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 4 && r.height > 4; };
  const out = { botones: [], inputs: [], combos: [] };
  document.querySelectorAll('button,[role=button]').forEach((b) => {
    if (!vis(b)) return;
    const t = (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\s+/g,' ').slice(0,44);
    if (t) out.botones.push(t);
  });
  document.querySelectorAll('textarea,input').forEach((i) => {
    out.inputs.push(`${i.tagName}[${i.type||'-'}] "${(i.placeholder||'').slice(0,50)}"`);
  });
  document.querySelectorAll('[role=combobox]').forEach((s) => { if (vis(s)) out.combos.push((s.innerText||'').trim().replace(/\s+/g,' ').slice(0,44)); });
  return out;
});
console.log('BOTONES:', [...new Set(inv.botones)].join(' | '));
console.log('INPUTS :', inv.inputs.join(' | '));
console.log('COMBOS :', [...new Set(inv.combos)].join(' | '));
await browser.close();
