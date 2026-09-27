import { abrir, cerrarOverlays } from './lote.mjs';
import fs from 'node:fs';
const SALIDA = '/home/matiigonzz/Descargas/GONVRA - flow/';
fs.mkdirSync(SALIDA, { recursive: true });

const { browser, page } = await abrir();
await cerrarOverlays(page);
await page.waitForTimeout(3000);

// tarjetas de video generadas, de más nuevas a más viejas
const cajas = await page.evaluate(() => {
  const out = [];
  document.querySelectorAll('span').forEach(s => {
    const t = (s.textContent || '').trim();
    if (!t || t.length < 8 || t.length > 60) return;
    let el = s;
    for (let i = 0; i < 10 && el; i++) {
      const r = el.getBoundingClientRect();
      if (r.width > 120 && r.height > 150) { out.push({ nombre: t, x: r.x + r.width/2, y: r.y + r.height/2 }); return; }
      el = el.parentElement;
    }
  });
  return out.slice(0, 30);
});
console.log('tarjetas visibles:', cajas.length);
console.log(cajas.map(c => c.nombre).slice(0, 14).join(' | '));
await browser.close();
