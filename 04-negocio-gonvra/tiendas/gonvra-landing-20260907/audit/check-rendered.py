from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import json, re

base='http://127.0.0.1:9297'
root=Path(__file__).parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls=[];self.ids=[];self.links=[];self.h1=0;self.offers=[];self.template_depth=0
    def handle_starttag(self,tag,attrs):
        if tag=='template':self.template_depth+=1
        if self.template_depth:return
        d=dict(attrs)
        if tag=='h1':self.h1+=1
        if 'id' in d:self.ids.append(d['id'])
        if tag=='a':self.links.append(d.get('href',''))
        if tag=='img':self.urls.append(d['src'])
        if tag=='source' and 'srcset' in d:self.urls.append(d['srcset'].split(',')[0].split()[0])
        if tag=='script' and 'gv-experience' in d.get('src',''):self.urls.append(d['src'])
        if tag=='link' and 'gv-experience' in d.get('href',''):self.urls.append(d['href'])
        if tag=='button' and 'data-gv-offer' in d:self.offers.append({'qty':d['data-qty'],'total':d['data-total']})
    def handle_endtag(self,tag):
        if tag=='template':self.template_depth-=1

all_urls=set();report={}
for name,path in [('home','/'),('product','/products/face-body-electric-shaver'),('cart','/cart'),('privacy','/policies/privacy-policy')]:
    with urlopen(base+path,timeout=40) as response:
        html=response.read().decode();status=response.status
    (root/(name+'-verified.html')).write_text(html)
    p=Page();p.feed(html)
    assert status==200 and 'Liquid error' not in html and 'Liquid syntax error' not in html,name
    assert '"id":148200751219' in html,name
    if name in ('home','product'):
        assert p.h1==1,(name,p.h1)
        assert not [a for a in p.links if not a or (a.startswith('#') and a[1:] not in p.ids)]
        assert len(p.ids)==len(set(p.ids)), (name,'duplicate IDs')
    all_urls.update(p.urls)
    report[name]={'status':status,'h1_count':p.h1,'offers':p.offers,'liquid_errors':0}
    if name=='product':(root/'rendered-offers.json').write_text(json.dumps(p.offers))

def check(url):
    absolute=urljoin(base,url)
    assert urlparse(absolute).hostname in ('127.0.0.1','gonvra.com','cdn.shopify.com','jm60sa-cp.myshopify.com')
    with urlopen(absolute,timeout=40) as response:
        status=response.status;response.read(1)
    assert status==200,absolute
    return {'url':url,'status':status}

with ThreadPoolExecutor(max_workers=4) as pool:report['assets']=list(pool.map(check,sorted(all_urls)))
(root/'verification.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps({k:v for k,v in report.items() if k!='assets'},ensure_ascii=False,indent=2))
print(f'{len(report["assets"])} image/style/script URLs: HTTP 200')
