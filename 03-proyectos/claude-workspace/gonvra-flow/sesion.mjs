// Copia liviana del perfil de Brave y abre Google Flow para ver si la sesión sigue viva.
import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const ORIGEN = path.join(os.homedir(), '.config/BraveSoftware/Brave-Browser');
const DESTINO = path.join(os.homedir(), '.cache/gonvra-brave');
const ARCHIVOS = ['Cookies', 'Login Data', 'Web Data', 'Preferences', 'Local State', 'Secure Preferences'];

function copiar() {
  fs.mkdirSync(path.join(DESTINO, 'Default'), { recursive: true });
  for (const f of ['Local State']) {
    const src = path.join(ORIGEN, f);
    if (fs.existsSync(src)) fs.copyFileSync(src, path.join(DESTINO, f));
  }
  for (const f of ARCHIVOS) {
    const src = path.join(ORIGEN, 'Default', f);
    if (fs.existsSync(src)) {
      try { fs.copyFileSync(src, path.join(DESTINO, 'Default', f)); } catch (e) { console.log('no pude copiar', f, e.message); }
    }
  }
}

copiar();

const ctx = await chromium.launchPersistentContext(DESTINO, {
  headless: true,
  executablePath: '/usr/bin/brave-browser',
  viewport: { width: 1440, height: 900 },
  args: ['--no-first-run', '--no-default-browser-check', '--disable-blink-features=AutomationControlled'],
});

const page = ctx.pages()[0] ?? (await ctx.newPage());
await page.goto('https://labs.google/fx/es/tools/flow', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(6000);
console.log('URL :', page.url());
console.log('TIT :', await page.title());
const texto = (await page.locator('body').innerText().catch(() => '')).slice(0, 700);
console.log('---- texto ----\n' + texto);
await page.screenshot({ path: '/tmp/flow.png', fullPage: false });
await ctx.close();
