import { chromium } from 'playwright-core';
import fs from 'node:fs';

const PROYECTO = 'https://flow.google.com/project/a6872b5e-edc6-4445-8616-7e517d274404';
const SALIDA = '/home/matiigonzz/Descargas/GONVRA - flow/';
const RIGIDEZ = 'CRITICAL: the device must stay rigid and geometrically identical to the reference image in every frame, same silhouette, same proportions, same lime-green button, same wide steel head. Do not bend, stretch, morph or redesign it. No logos, no text, no brand marks.';

export const TAREAS = [
  { id: 'rostro',   ref: 'ref-7-rostro.jpg',
    prompt: `Animate this exact photograph with minimal motion. The man slides the shaver upward along his jawline ONE single slow continuous stroke, and the stubble is visibly cut away behind the head leaving clean skin. The camera stays almost completely still. Keep the grip exactly as in the photo: the steel foil head at the TOP touching the skin, black body pointing DOWN. ${RIGIDEZ} Natural warm bathroom light, realistic skin texture, photorealistic.` },
  { id: 'kit',      ref: 'ref-1-kit-flatlay.jpg',
    prompt: `Animate this exact top-down photograph. Very slow camera push-in over the laid-out kit with a soft light sweep crossing the surface. Everything stays exactly where it is, no item moves. ${RIGIDEZ} Soft natural light, muted earthy palette, photorealistic.` },
  { id: 'mesada',   ref: 'ref-6-mesada-vertical.jpg',
    prompt: `Animate this exact photograph. Slow cinematic push-in toward the device standing on the marble counter, with soft morning light shifting gently across the surface. The device does not move. ${RIGIDEZ} Photorealistic.` },
  { id: 'pack3',    ref: 'ref-4-tres-unidades.jpg',
    prompt: `Animate this exact packshot. The three identical units rotate slowly and together on the ivory surface, with a subtle lime accent light passing across them. ${RIGIDEZ} Clean studio product-commercial look.` },
  { id: 'giro',     ref: 'ref-5-packshot.jpg',
    prompt: `Animate this exact packshot. The device rotates slowly on its vertical axis over a seamless ivory background, soft studio light with a gentle highlight travelling along the steel head. ${RIGIDEZ}` },
  { id: 'counter2', ref: 'ref-2-counter.jpg',
    prompt: `Animate this exact photograph. Extremely slow dolly toward the device on the bathroom counter, with warm light drifting and soft depth of field. The device stays perfectly still. ${RIGIDEZ} Photorealistic.` },
];

export async function abrir() {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const ctx = browser.contexts()[0];
  let page = ctx.pages().find(p => p.url().includes('flow.google.com/project'));
  if (!page) { page = await ctx.newPage(); await page.goto(PROYECTO, { waitUntil:'domcontentloaded', timeout:60000 }); await page.waitForTimeout(9000); }
  await page.bringToFront();
  return { browser, page };
}

export async function cerrarOverlays(page) {
  for (let i=0;i<4;i++){
    const hay = await page.evaluate(()=>!!document.querySelector('.cdk-overlay-backdrop-showing'));
    if(!hay) return;
    await page.keyboard.press('Escape'); await page.waitForTimeout(1000);
  }
}

async function abrirMenu(page) {
  for (let intento = 0; intento < 4; intento++) {
    if (await page.getByText('Subir archivo multimedia').count()) return true;
    // el "+" de la barra de petición está abajo; el otro "add" está arriba/izquierda
    const pos = await page.evaluate(() => {
      const b = [...document.querySelectorAll('button,[role=button]')]
        .filter(x => (x.innerText || '').trim() === 'add')
        .map(x => { const r = x.getBoundingClientRect(); return { x: r.x + r.width/2, y: r.y + r.height/2, w: r.width }; })
        .filter(p => p.w > 10);
      if (!b.length) return null;
      b.sort((a, c) => c.y - a.y);          // el más abajo primero
      return b[0];
    });
    if (!pos) { await page.waitForTimeout(1200); continue; }
    await page.mouse.click(pos.x, pos.y);
    await page.waitForTimeout(2800);
    if (await page.getByText('Subir archivo multimedia').count()) return true;
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(1000);
  }
  return false;
}

export async function subirYAdjuntar(page, archivo) {
  const nombre = archivo.split('/').pop();

  // ¿ya está en la biblioteca?
  let existe = await page.evaluate((n)=>[...document.querySelectorAll('span')].some(e=>(e.textContent||'').trim()===n), nombre);

  if (!existe) {
    if (!(await abrirMenu(page))) throw new Error('no pude abrir el menú');
    // el botón real es el que tiene aria-describedby apuntando a ese tooltip
    const punto = await page.evaluate(() => {
      const tip = [...document.querySelectorAll('[role=tooltip]')]
        .find(t => (t.textContent||'').trim() === 'Subir archivo multimedia');
      if (!tip) return null;
      const btn = document.querySelector(`[aria-describedby~="${tip.id}"]`);
      if (!btn) return null;
      const r = btn.getBoundingClientRect();
      return { x: r.x + r.width/2, y: r.y + r.height/2 };
    });
    if (!punto) throw new Error('no encontré el botón de subir');
    const [fc] = await Promise.all([
      page.waitForEvent('filechooser', { timeout: 30000 }),
      page.mouse.click(punto.x, punto.y),
    ]);
    await fc.setFiles(archivo);
    console.log('  subiendo…');
    for (let i = 0; i < 24; i++) {
      await page.waitForTimeout(2500);
      existe = await page.evaluate((n)=>[...document.querySelectorAll('span')].some(e=>(e.textContent||'').trim()===n), nombre);
      if (existe) break;
    }
    if (!existe) throw new Error('la subida no apareció en la biblioteca');
  }

  if (!(await page.getByText('Subir archivo multimedia').count())) await abrirMenu(page);
  await page.waitForTimeout(1200);

  const caja = await page.evaluate((n) => {
    const sp=[...document.querySelectorAll('span')].filter(e=>(e.textContent||'').trim()===n);
    if(!sp.length) return null;
    let el=sp[0];
    for(let i=0;i<10&&el;i++){ const r=el.getBoundingClientRect(); if(r.width>120&&r.height>120) { el.scrollIntoView({block:'center'}); const q=el.getBoundingClientRect(); return {x:q.x+q.width/2,y:q.y+q.height/2}; } el=el.parentElement; }
    return null;
  }, nombre);
  if (!caja) throw new Error('no encontré la tarjeta de ' + nombre);
  await page.mouse.move(caja.x, caja.y);
  await page.waitForTimeout(1800);
  await page.getByRole('button',{name:/Añadir a petición/i}).first().click({ force:true, timeout:15000 });
  await page.waitForTimeout(3000);
}

export async function escribirYGenerar(page, prompt) {
  await cerrarOverlays(page);
  await page.evaluate(()=>{
    const ed=[...document.querySelectorAll('[contenteditable=true]')].filter(e=>e.getBoundingClientRect().width>200);
    if(ed.length) ed[0].focus();
  });
  await page.waitForTimeout(700);
  await page.keyboard.type(prompt, { delay: 2 });
  await page.waitForTimeout(2200);
  await page.locator('button:has-text("arrow_forward")').last().click({ timeout:20000, force:true });
}
