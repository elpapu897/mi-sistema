import { chromium } from 'playwright-core';
const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
for (const [i, ctx] of browser.contexts().entries())
  for (const [j, p] of ctx.pages().entries())
    console.log(`${i}.${j}  ${p.url().slice(0,110)}`);
await browser.close();
