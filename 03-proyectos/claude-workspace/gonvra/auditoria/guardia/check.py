from pathlib import Path
import re
s=Path('/tmp/gonvra_home.html').read_text(errors='ignore')
terms=['3919766821491073','26889872433954472','PageView','ViewContent','fbq','facebook','pixel','Meta']
for t in terms:
    print('---',t)
    for m in list(re.finditer(re.escape(t),s,re.I))[:8]:
        print(' '.join(s[max(0,m.start()-180):m.end()+260].split()))
print('--- links críticos')
for href in sorted(set(re.findall(r'href=["\']([^"\']+)',s,re.I))):
    if any(x in href.lower() for x in ['shipping','contact','policy','checkout']): print(href)
