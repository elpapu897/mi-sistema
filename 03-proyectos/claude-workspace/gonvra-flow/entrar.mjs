import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = await ctx.newPage();
await page.goto('https://labs.google/fx/tools/flow', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(6000);

if (page.url().includes('accounts.google.com')) {
  console.log('→ eligiendo cuenta…');
  const cuenta = page.getByText('natividadvega42@gmail.com').first();
  await cuenta.click({ timeout: 20000 }).catch(async () => {
    await page.locator('[data-identifier="natividadvega42@gmail.com"]').click({ timeout: 15000 });
  });
  await page.waitForTimeout(9000);
  // posible pantalla de consentimiento
  for (const t of ['Continuar', 'Continue', 'Permitir', 'Allow', 'Aceptar']) {
    const b = page.getByRole('button', { name: t });
    if (await b.count().catch(() => 0)) { await b.first().click().catch(() => {}); await page.waitForTimeout(6000); break; }
  }
}

await page.waitForTimeout(8000);
console.log('URL   →', page.url());
console.log('TÍTULO→', await page.title());
console.log('---- pantalla ----');
console.log((await page.locator('body').innerText().catch(() => '')).slice(0, 900));
await page.screenshot({ path: '/tmp/flow-app.png' });
await browser.close();
