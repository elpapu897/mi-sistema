import json,re
from html import unescape
from pathlib import Path

for fname in ['bacan-home.html','gadnic-list.html','philips-list.html']:
    text=Path(__file__).with_name(fname).read_text(errors='ignore')
    print('\n===',fname,'===')
    if fname=='bacan-home.html':
        for m in sorted(set(re.findall(r'href=["\']([^"\']*(?:razor|body)[^"\']*)',text,re.I))): print('URL',unescape(m))
        for m in re.finditer(r'item_name":"([^"]*(?:Razor|Body)[^"]*)"[^}]{0,250}?price":([0-9.]+)',text,re.I): print('ITEM',m.group(1),m.group(2))
        for pat in [r'Razor Body.{0,700}',r'83990.{0,700}']:
            mm=re.search(pat,text,re.I|re.S)
            if mm: print('SNIP',re.sub(r'<[^>]+>',' ',unescape(mm.group(0)))[:1000])
    elif fname=='gadnic-list.html':
        mm=re.search(r'dataLayer\s*=\s*(\[.*?\]);',text,re.S)
        if mm:
            data=json.loads(mm.group(1))[0]
            for x in data.get('id-skus',[]): print(json.dumps(x,ensure_ascii=False))
    else:
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
            try:
                d=json.loads(unescape(block))
                if isinstance(d,dict) and d.get('@type')=='ItemList':
                    for e in d.get('itemListElement',[]):
                        x=e.get('item',{}); print(json.dumps({'name':x.get('name'),'url':x.get('@id'),'offers':x.get('offers')},ensure_ascii=False))
            except Exception: pass
