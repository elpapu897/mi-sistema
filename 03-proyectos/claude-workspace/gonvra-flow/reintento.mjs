import { TAREAS, abrir, subirYAdjuntar, escribirYGenerar, cerrarOverlays } from './lote.mjs';
const REFS = '/home/matiigonzz/Claude/gonvra-brand/flow-refs/';
const { browser, page } = await abrir();
for (const t of TAREAS.filter(t => ['kit','pack3'].includes(t.id))) {
  for (let intento = 1; intento <= 3; intento++) {
    try {
      console.log(`▸ ${t.id} (intento ${intento})`);
      await cerrarOverlays(page); await page.waitForTimeout(2500);
      await subirYAdjuntar(page, REFS + t.ref);
      await escribirYGenerar(page, t.prompt);
      console.log('  ✓ lanzada'); await page.waitForTimeout(14000);
      break;
    } catch (e) { console.log('  ✗', e.message.split('\n')[0].slice(0,70)); await cerrarOverlays(page); await page.waitForTimeout(4000); }
  }
}
await browser.close();
