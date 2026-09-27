import json,re
p='/home/matiigonzz/Claude/gonvra2/espia/facebook-rasuradora.json'
data=json.load(open(p))
text=data['text']
blocks=re.split(r'(?=Activo\nIdentificador de la biblioteca:)',text)
for b in blocks:
    low=b.lower()
    if any(k in low for k in ['rasur','afeit','recort','vello','zona íntima','zona intima','corporal']):
        print('---')
        print(b[:2500])
