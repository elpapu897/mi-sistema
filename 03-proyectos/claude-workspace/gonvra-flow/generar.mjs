import { chromium } from 'playwright-core';

const REF = '/home/matiigonzz/Claude/gonvra-brand/flow-refs/ref-3-uso-brazo.jpg';
const PROMPT = `Animate this exact photograph with minimal motion. The hand slides the shaver down the forearm ONE single slow continuous stroke, revealing a clean trimmed strip behind it. The camera stays almost completely still, only a tiny handheld drift. CRITICAL: the device must stay rigid and geometrically identical to the reference image in every frame — same silhouette, same proportions, same lime-green button, same wide steel head. Do not bend, stretch, morph or redesign it. No logos, no text, no brand marks. Natural window light, realistic skin texture, photorealistic.`;

const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = ctx.pages().find(p => p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront(); await page.waitForTimeout(1500);

// menú ya abierto → subir archivo
const subir = page.getByText('Subir archivo multimedia').first();
if (await subir.count()) {
  const [fc] = await Promise.all([
    page.waitForEvent('filechooser', { timeout: 20000 }),
    subir.click(),
  ]);
  await fc.setFiles(REF);
  console.log('→ frame subido');
  await page.waitForTimeout(9000);
} else {
  console.log('menú cerrado, lo reabro');
}

// escribir la petición
const campo = page.locator('textarea, input[type=text]').filter({ hasNot: page.locator('[readonly]') });
const n = await campo.count();
console.log('campos de texto:', n);
for (let i = 0; i < n; i++) {
  const c = campo.nth(i);
  if (await c.isVisible().catch(() => false)) {
    await c.click();
    await c.fill(PROMPT).catch(async () => { await page.keyboard.type(PROMPT, { delay: 4 }); });
    console.log('→ petición escrita en campo', i);
    break;
  }
}
await page.waitForTimeout(2000);
await page.screenshot({ path: '/tmp/flow-listo.png', timeout: 60000, animations: 'disabled',
  clip: { x: 0, y: 560, width: 1440, height: 340 } }).catch(e => console.log('sin captura'));
await browser.close();
