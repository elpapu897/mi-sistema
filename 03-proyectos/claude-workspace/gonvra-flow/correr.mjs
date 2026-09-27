import { TAREAS, abrir, subirYAdjuntar, escribirYGenerar, cerrarOverlays } from './lote.mjs';
const REFS = '/home/matiigonzz/Claude/gonvra-brand/flow-refs/';
const soloId = process.argv[2];
const lista = soloId ? TAREAS.filter(t=>t.id===soloId) : TAREAS;

const { browser, page } = await abrir();
for (const t of lista) {
  try {
    console.log(`\n▸ ${t.id}`);
    await cerrarOverlays(page);
    await subirYAdjuntar(page, REFS + t.ref);
    console.log('  frame adjunto');
    await escribirYGenerar(page, t.prompt);
    console.log('  ✓ generación lanzada');
    await page.waitForTimeout(12000);
  } catch (e) {
    console.log('  ✗ error:', e.message.split('\n')[0].slice(0,90));
    await cerrarOverlays(page);
  }
}
console.log('\nTodas lanzadas. Se generan en paralelo en Flow.');
await browser.close();
