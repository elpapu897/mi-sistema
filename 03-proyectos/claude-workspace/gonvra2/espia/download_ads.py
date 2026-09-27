import json, re, pathlib, requests
p=pathlib.Path('/home/matiigonzz/Claude/gonvra2/espia/facebook-videos.json')
data=json.load(open(p))
ids=['1642088480137981','1531068505162083','1655130648858808']
outdir=p.parent/'videos'; outdir.mkdir(exist_ok=True)
for adid in ids:
    item=next(x for x in data if adid in x.get('text',''))
    r=requests.get(item['src'],headers={'User-Agent':'Mozilla/5.0','Referer':'https://www.facebook.com/'},timeout=90)
    r.raise_for_status()
    fn=outdir/f'{adid}.mp4'
    fn.write_bytes(r.content)
    print(adid,fn,len(r.content))
