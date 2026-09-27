import json,re,urllib.parse,urllib.request
from html import unescape
qs=['rasuradora corporal hombre argentina tienda','afeitadora corporal hombre argentina oferta','recortadora barba argentina instagram','"rasuradora corporal" "envío gratis"','"Body Groomer" Argentina precio','site:youtube.com rasuradora corporal argentina']
out={}
for q in qs:
 u='https://www.google.com/search?hl=es&gl=ar&num=20&q='+urllib.parse.quote(q)
 req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128 Safari/537.36'})
 try:
  html=urllib.request.urlopen(req,timeout=25).read().decode('utf-8','ignore')
  links=[]
  for m in re.finditer(r'<a href="/url\?q=([^&"]+)[^"]*"[^>]*>(.*?)</a>',html,re.S):
   url=urllib.parse.unquote(m.group(1)); title=re.sub('<[^>]+>',' ',m.group(2)); title=' '.join(unescape(title).split())
   if title and url.startswith('http'): links.append({'title':title,'url':url})
  if not links:
   for m in re.finditer(r'<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>',html,re.S):
    url=unescape(m.group(1)); title=' '.join(unescape(re.sub('<[^>]+>',' ',m.group(2))).split())
    if title and 'google.' not in url: links.append({'title':title,'url':url})
  out[q]=links[:20]
 except Exception as e: out[q]={'error':str(e)}
print(json.dumps(out,ensure_ascii=False,indent=2))
