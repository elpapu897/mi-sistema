from pathlib import Path
import re
from html import unescape
try:
 from bs4 import BeautifulSoup
except Exception:
 BeautifulSoup=None
for f in ['bacan-product.html','gadnic-product.html','philips-product.html']:
 raw=Path(__file__).with_name(f).read_text(errors='ignore')
 text=BeautifulSoup(raw,'html.parser').get_text(' ',strip=True) if BeautifulSoup else re.sub(r'<[^>]+>',' ',raw)
 text=' '.join(unescape(text).split())
 print('\n===',f,'===')
 for term in ['83.990','119.990','67.192','55.099','86.299','103.559','cuotas','envío gratis','envios gratis','transferencia']:
  for m in list(re.finditer(re.escape(term),text,re.I))[:5]: print(term, text[max(0,m.start()-140):m.end()+220])
