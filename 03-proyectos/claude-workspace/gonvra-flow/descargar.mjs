import { abrir, cerrarOverlays } from './lote.mjs';
import fs from 'node:fs';
const SALIDA = '/home/matiigonzz/Descargas/GONVRA - flow/';
fs.mkdirSync(SALIDA, { recursive: true });

const { browser, page } = await abrir();
await cerrarOverlays(page);
await page.waitForTimeout(2500);

// tarjetas de la grilla principal (x > 280) que son videos
const tiles = await page.evaluate(() => {
  const out = [];
  document.querySelectorAll('video, [class*=tile], [class*=card]').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.x < 280 || r.width < 120 || r.height < 150) return;
    const txt = (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    out.push({ x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2), txt });
  });
  const vistos = new Set();
  return out.filter(t => { const k = `${t.x},${t.y}`; if (vistos.has(k)) return false; vistos.add(k); return true; }).slice(0, 12);
});
console.log('tarjetas en grilla:', tiles.length);

let n = 0;
for (const t of tiles) {
  try {
    await page.mouse.click(t.x, t.y);
    await page.waitForTimeout(5000);
    const tieneVideo = await page.evaluate(() => !!document.querySelector('video'));
    if (!tieneVideo) { await page.keyboard.press('Escape'); await page.waitForTimeout(1500); continue; }

    // botón descargar
    const pt = await page.evaluate(() => {
      const tip = [...document.querySelectorAll('[role=tooltip]')].find(x => /descarg/i.test(x.textContent || ''));
      let btn = tip ? document.querySelector(`[aria-describedby~="${tip.id}"]`) : null;
      if (!btn) btn = [...document.querySelectorAll('button')].find(b => (b.innerText||'').trim() === 'download');
      if (!btn) return null;
      const r = btn.getBoundingClientRect();
      return { x: r.x + r.width/2, y: r.y + r.height/2 };
    });
    if (!pt) { await page.keyboard.press('Escape'); await page.waitForTimeout(1500); continue; }
    await page.mouse.click(pt.x, pt.y);
    await page.waitForTimeout(2500);

    const [dl] = await Promise.all([
      page.waitForEvent('download', { timeout: 90000 }).catch(() => null),
      page.getByText('Tamaño original').first().click({ timeout: 12000 }).catch(() => {}),
    ]);
    if (dl) {
      n++;
      const destino = SALIDA + `flow-${String(n).padStart(2,'0')}-${(dl.suggestedFilename()||'clip.mp4')}`.replace(/\s+/g,'-');
      await dl.saveAs(destino);
      console.log('✓', destino.split('/').pop());
    }
    await page.keyboard.press('Escape'); await page.waitForTimeout(2500);
  } catch (e) {
    console.log('✗', e.message.split('\n')[0].slice(0,60));
    await page.keyboard.press('Escape').catch(()=>{}); await page.waitForTimeout(2000);
  }
}
console.log('descargados:', n);
await browser.close();
