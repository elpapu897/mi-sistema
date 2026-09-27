import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = await ctx.newPage();
await page.goto('https://labs.google/fx/tools/flow', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(7000);

// crear proyecto nuevo
const nuevo = page.getByText('Nuevo proyecto').first();
if (await nuevo.count()) { await nuevo.click(); console.log('→ click en Nuevo proyecto'); }
await page.waitForTimeout(9000);
console.log('URL →', page.url());

// inventario de controles
const inventario = await page.evaluate(() => {
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 4 && r.height > 4; };
  const out = { botones: [], inputs: [], selects: [], textos: [] };
  document.querySelectorAll('button,[role=button]').forEach((b) => {
    if (!vis(b)) return;
    const t = (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 50);
    if (t) out.botones.push(t);
  });
  document.querySelectorAll('textarea,input').forEach((i) => {
    if (!vis(i) && i.type !== 'file') return;
    out.inputs.push(`${i.tagName}[type=${i.type || '-'}] ph="${(i.placeholder || '').slice(0, 60)}"`);
  });
  document.querySelectorAll('[role=combobox],select').forEach((s) => {
    if (!vis(s)) return;
    out.selects.push((s.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 50));
  });
  return out;
});
console.log('BOTONES:', JSON.stringify([...new Set(inventario.botones)], null, 0));
console.log('INPUTS :', JSON.stringify(inventario.inputs, null, 0));
console.log('SELECTS:', JSON.stringify([...new Set(inventario.selects)], null, 0));
await page.screenshot({ path: '/tmp/flow-proyecto.png' });
await browser.close();
