import json,requests,pathlib,re
urls={
'voltra':'https://voltra.com.ar/products/afeitadora-anti-cortes-100-sumergible-voltra%C2%AE',
'bacan':'https://bacanbymantra.com/sale-bacan/',
'myhuevos':'https://myhuevos.com.ar/products/rasuradora-myhuevos%C2%AE-4-0',
}
out={}
for name,url in urls.items():
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=45)
    out[name]={'status':r.status_code,'url':r.url,'html':r.text[:1000000]}
    try:
        j=requests.get(url+'.js',headers={'User-Agent':'Mozilla/5.0'},timeout=45)
        out[name]['js_status']=j.status_code
        out[name]['product_json']=j.json() if j.status_code==200 else None
    except Exception as e: out[name]['js_error']=str(e)
path=pathlib.Path('/home/matiigonzz/Claude/gonvra2/espia/product-pages.json')
path.write_text(json.dumps(out,ensure_ascii=False),encoding='utf-8')
for name,d in out.items():
    pj=d.get('product_json')
    if pj:
        print(name,d['status'],pj.get('title'),pj.get('price'),pj.get('compare_at_price'),[(v.get('title'),v.get('price'),v.get('compare_at_price'),v.get('available')) for v in pj.get('variants',[])])
    else:
        html=d['html']
        vals=[]
        for pat in [r'\$\s?[\d\.]+(?:,\d+)?',r'price[^\d]{0,30}([\d\.]+(?:,\d+)?)']:
            vals += re.findall(pat,html,re.I)[:20]
        print(name,d['status'],'matches',vals[:30])
