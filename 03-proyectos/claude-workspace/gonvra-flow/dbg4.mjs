import { abrir } from './lote.mjs';
const { browser, page } = await abrir();
await page.keyboard.press('Escape'); await page.waitForTimeout(1200);

const pos = await page.evaluate(() => {
  const b=[...document.querySelectorAll('button,[role=button]')]
    .filter(x=>(x.innerText||'').trim()==='add')
    .map(x=>{const r=x.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2,w:r.width};})
    .filter(p=>p.w>10).sort((a,c)=>c.y-a.y);
  return b[0]||null;
});
console.log('+ en', JSON.stringify(pos));
await page.mouse.click(pos.x, pos.y);
await page.waitForTimeout(3000);
console.log('menú abierto:', await page.getByText('Subir archivo multimedia').count());

const el = page.getByText('Subir archivo multimedia').first();
await el.click();
await page.waitForTimeout(3500);
const despues = await page.evaluate(()=>{
  const vis=(e)=>{const r=e.getBoundingClientRect();return r.width>20&&r.height>14;};
  const o=[]; document.querySelectorAll('*').forEach(e=>{ if(!vis(e)||e.children.length)return;
    const t=(e.textContent||'').trim(); if(t&&t.length>3&&t.length<50) o.push(t); });
  return { textos:[...new Set(o)].slice(0,18), inputs:document.querySelectorAll('input[type=file]').length };
});
console.log('inputs file ahora:', despues.inputs);
console.log('textos:\n  ' + despues.textos.join('\n  '));
await browser.close();
