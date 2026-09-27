import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

QUERIES = [
    '"rasuradora corporal" Argentina tienda',
    '"afeitadora corporal" hombre Argentina oferta',
    '"recortadora corporal" hombre Argentina oferta',
    'site:youtube.com "rasuradora corporal"',
    'site:tiktok.com rasuradora corporal argentina',
    'site:instagram.com rasuradora corporal argentina',
    'site:facebook.com rasuradora corporal argentina',
    'Body Groomer Argentina precio',
]
out={}
for q in QUERIES:
    url='https://www.bing.com/search?format=rss&q='+urllib.parse.quote(q)
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req,timeout=25) as r: raw=r.read()
        root=ET.fromstring(raw)
        out[q]=[{'title':i.findtext('title'),'url':i.findtext('link'),'snippet':i.findtext('description')} for i in root.findall('.//item')[:15]]
    except Exception as e: out[q]={'error':str(e)}
print(json.dumps(out,ensure_ascii=False,indent=2))
