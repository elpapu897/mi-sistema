import { TAREAS, abrir, subirYAdjuntar, escribirYGenerar, cerrarOverlays } from './lote.mjs';
const REFS = '/home/matiigonzz/Claude/gonvra-brand/flow-refs/';
const { browser, page } = await abrir();
for (const t of TAREAS.filter(t => t.id !== 'rostro')) {
  try {
    console.log(`▸ ${t.id}`);
    await cerrarOverlays(page);
    await subirYAdjuntar(page, REFS + t.ref);
    await escribirYGenerar(page, t.prompt);
    console.log('  ✓ lanzada');
    await page.waitForTimeout(14000);
  } catch (e) { console.log('  ✗', e.message.split('\n')[0].slice(0,80)); await cerrarOverlays(page); }
}
await browser.close();
