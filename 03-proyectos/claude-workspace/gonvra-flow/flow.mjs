// Se conecta al Brave que ya está abierto (con --remote-debugging-port=9222)
import { chromium } from 'playwright-core';

export async function conectar() {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const ctx = browser.contexts()[0];
  return { browser, ctx };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const { browser, ctx } = await conectar();
  const page = await ctx.newPage();
  await page.goto('https://labs.google/fx/tools/flow', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(8000);
  console.log('URL   →', page.url());
  console.log('TÍTULO→', await page.title());
  const txt = (await page.locator('body').innerText().catch(() => '')).slice(0, 800);
  console.log('---- lo que veo ----\n' + txt);
  await page.screenshot({ path: '/tmp/flow-app.png' });
  await page.close();
  await browser.close();
}
