import asyncio, json, sys, urllib.request
import websockets

async def main():
    tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9223/json'))
    tab=next((t for t in tabs if t.get('type')=='page'), tabs[0])
    uri=tab['webSocketDebuggerUrl']
    async with websockets.connect(uri, max_size=50_000_000) as ws:
        i=0
        async def cmd(method, params=None):
            nonlocal i
            i+=1
            await ws.send(json.dumps({'id':i,'method':method,'params':params or {}}))
            while True:
                msg=json.loads(await ws.recv())
                if msg.get('id')==i:
                    return msg
        await cmd('Runtime.enable')
        await asyncio.sleep(15)
        res=await cmd('Runtime.evaluate',{'expression':'JSON.stringify({title:document.title,url:location.href,text:document.body.innerText,html:document.documentElement.outerHTML.slice(0,200000)})','returnByValue':True})
        value=res.get('result',{}).get('result',{}).get('value','')
        print(value)

asyncio.run(main())
