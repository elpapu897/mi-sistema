from pathlib import Path
import re, json
s=Path('/tmp/gonvra_checkout2.html').read_text(errors='ignore')
for term in ['Mercado Pago','PayPal','tarjeta','Método de pago','Envío gratis','Argentina']:
 print('\n---',term)
 for m in list(re.finditer(term,s,re.I))[:8]: print(' '.join(re.sub('<[^>]+>',' ',s[max(0,m.start()-180):m.end()+300]).split()))
print('\nADD RESPONSE')
print(Path('/tmp/gonvra_added.json').read_text(errors='ignore')[:1000])
