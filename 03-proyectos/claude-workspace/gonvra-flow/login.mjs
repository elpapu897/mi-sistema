import { chromium } from 'playwright-core';
import os from 'node:os'; import path from 'node:path';
const ctx = await chromium.launchPersistentContext(path.join(os.homedir(), '.cache/gonvra-brave'), {
  headless: true, executablePath: '/usr/bin/brave-browser',
  viewport: { width: 1440, height: 900 },
  args: ['--no-first-run','--no-default-browser-check','--disable-blink-features=AutomationControlled'],
});
const page = ctx.pages()[0] ?? await ctx.newPage();
// ¿hay sesión de Google?
await page.goto('https://myaccount.google.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(5000);
console.log('cuenta →', page.url());
console.log('titulo →', await page.title());
const t = (await page.locator('body').innerText().catch(()=>'')).slice(0,300).replace(/\n+/g,' | ');
console.log('texto  →', t);
await ctx.close();
