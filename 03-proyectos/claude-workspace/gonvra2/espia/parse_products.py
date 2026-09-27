import json,re,html
p='/home/matiigonzz/Claude/gonvra2/espia/product-pages.json'
d=json.load(open(p))
for name,x in d.items():
    raw=x['html']
    txt=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',raw)))
    print('\n###',name)
    for term in ['envío gratis','envio gratis','cuotas','transferencia','20%','83.990','67.192','137.880','74.900','200.000','139.900']:
        for m in list(re.finditer(re.escape(term),txt,re.I))[:3]:
            print(term,':',txt[max(0,m.start()-120):m.end()+180])
    pj=x.get('product_json')
    if pj:
        desc=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',pj.get('description',''))))
        print('description:',desc[:2000])
