import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const page = browser.contexts()[0].pages().find(p=>p.url().includes('flow.google.com'));
await page.bringToFront(); await page.waitForTimeout(1500);

const abierto = await page.evaluate(()=>!!document.querySelector('.cdk-overlay-backdrop-showing') || !!document.querySelector('[role=menu]'));
if (!abierto) {
  await page.locator('button:has-text("download"), [aria-label*="escarg"]').last().click({ timeout: 15000 });
  await page.waitForTimeout(2500);
}
const [dl] = await Promise.all([
  page.waitForEvent('download', { timeout: 90000 }).catch(()=>null),
  page.getByText('Tamaño original').first().click({ timeout: 15000 }).catch(()=>console.log('no pude clickear 720p')),
]);
if (dl) {
  const destino = '/home/matiigonzz/Descargas/GONVRA - flow/brazo-corregido.mp4';
  await dl.saveAs(destino);
  console.log('✓ DESCARGADO →', destino);
} else console.log('✗ sin descarga');
await browser.close();
