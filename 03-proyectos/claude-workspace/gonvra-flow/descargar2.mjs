import { abrir, cerrarOverlays } from './lote.mjs';
import fs from 'node:fs';
const SALIDA = '/home/matiigonzz/Descargas/GONVRA - flow/';
fs.mkdirSync(SALIDA, { recursive: true });
const { browser, page } = await abrir();
await cerrarOverlays(page); await page.waitForTimeout(2000);

const tiles = await page.evaluate(()=>[...document.querySelectorAll('img')]
  .filter(i=>{const r=i.getBoundingClientRect();return r.width>140&&r.height>180&&r.x>200;})
  .map(i=>{const r=i.getBoundingClientRect();return {x:Math.round(r.x+r.width/2),y:Math.round(r.y+r.height/2)};})
  .slice(0,10));
console.log('tarjetas:', tiles.length);

let n=0;
for (const t of tiles) {
  try {
    await page.mouse.click(t.x, t.y);
    await page.waitForTimeout(6000);
    if (!(await page.evaluate(()=>!!document.querySelector('video')))) {
      await page.keyboard.press('Escape'); await page.waitForTimeout(2000); continue;
    }
    const pt = await page.evaluate(()=>{
      const tip=[...document.querySelectorAll('[role=tooltip]')].find(x=>/descarg/i.test(x.textContent||''));
      let b = tip ? document.querySelector(`[aria-describedby~="${tip.id}"]`) : null;
      if(!b) b=[...document.querySelectorAll('button')].find(x=>(x.innerText||'').trim()==='download');
      if(!b) return null; const r=b.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2};
    });
    if(!pt){ await page.keyboard.press('Escape'); await page.waitForTimeout(2000); continue; }
    await page.mouse.click(pt.x, pt.y); await page.waitForTimeout(2600);
    const [dl] = await Promise.all([
      page.waitForEvent('download',{timeout:120000}).catch(()=>null),
      page.getByText('Tamaño original').first().click({timeout:12000}).catch(()=>{}),
    ]);
    if (dl) { n++; const d=SALIDA+`flow-${String(n).padStart(2,'0')}.mp4`; await dl.saveAs(d); console.log('✓', d.split('/').pop()); }
    await page.keyboard.press('Escape'); await page.waitForTimeout(3000);
  } catch(e){ console.log('✗', e.message.split('\n')[0].slice(0,60)); await page.keyboard.press('Escape').catch(()=>{}); await page.waitForTimeout(2000); }
}
console.log('total descargados:', n);
await browser.close();
