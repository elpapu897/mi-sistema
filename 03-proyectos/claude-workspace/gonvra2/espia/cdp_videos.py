import asyncio,json,urllib.request
import websockets

JS=r'''(() => {
  const out=[];
  for (const v of document.querySelectorAll('video')) {
    let e=v;
    while(e && !(e.innerText||'').includes('Identificador de la biblioteca:')) e=e.parentElement;
    let card=e;
    while(card && card.parentElement && (card.parentElement.innerText||'').includes('Identificador de la biblioteca:') && (card.parentElement.innerText||'').length<5000) card=card.parentElement;
    const links=[...(card||v.parentElement).querySelectorAll('a')].map(a=>({text:(a.innerText||'').trim(),href:a.href})).filter(x=>x.href);
    out.push({src:v.currentSrc||v.src,poster:v.poster,text:(card?.innerText||'').slice(0,5000),links});
  }
  return out;
})()'''

async def main():
    tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9223/json'))
    tab=next(t for t in tabs if t.get('type')=='page' and 'facebook.com/ads/library' in t.get('url',''))
    async with websockets.connect(tab['webSocketDebuggerUrl'],max_size=100_000_000) as ws:
        i=0
        async def cmd(method,params=None):
            nonlocal i;i+=1
            await ws.send(json.dumps({'id':i,'method':method,'params':params or {}}))
            while True:
                m=json.loads(await ws.recv())
                if m.get('id')==i:return m
        await cmd('Runtime.enable')
        # Scroll to ensure more cards and video sources load.
        for _ in range(10):
            await cmd('Runtime.evaluate',{'expression':'window.scrollBy(0,1400)'})
            await asyncio.sleep(2)
        res=await cmd('Runtime.evaluate',{'expression':JS,'returnByValue':True,'awaitPromise':True})
        print(json.dumps(res['result']['result'].get('value',[]),ensure_ascii=False,indent=2))
asyncio.run(main())
