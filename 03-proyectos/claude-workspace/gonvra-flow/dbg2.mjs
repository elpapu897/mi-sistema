import { abrir, cerrarOverlays } from './lote.mjs';
const { browser, page } = await abrir();
await page.waitForTimeout(2000);
// ¿qué hay en la biblioteca ahora?
const nombres = await page.evaluate(()=>{
  const o=[]; document.querySelectorAll('span,div').forEach(e=>{
    if(e.children.length) return;
    const t=(e.textContent||'').trim();
    if(/\.(jpg|png|mp4)$/i.test(t)) o.push(t);
  });
  return [...new Set(o)];
});
console.log('archivos en biblioteca:', nombres.join(' | ') || 'ninguno');
const inputs = await page.evaluate(()=>[...document.querySelectorAll('input[type=file]')].map(i=>({accept:i.accept||'-', hidden:i.offsetParent===null, name:i.name||'-'})));
console.log('inputs file:', JSON.stringify(inputs));
await page.screenshot({path:'/tmp/dbg.png',timeout:60000,animations:'disabled'}).catch(()=>console.log('sin captura'));
await browser.close();
