import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
const ctx = browser.contexts()[0];
const page = ctx.pages().find(p => p.url().includes('flow.google.com/project/a6872b5e'));
await page.bringToFront(); await page.waitForTimeout(2500);
const vp = page.viewportSize() || { width: 1440, height: 900 };
await page.screenshot({ path: '/tmp/flow-ed.png', timeout: 90000, animations: 'disabled',
  clip: { x: 0, y: Math.max(0, vp.height - 340), width: vp.width, height: 340 } });
console.log('viewport', vp);
await browser.close();
