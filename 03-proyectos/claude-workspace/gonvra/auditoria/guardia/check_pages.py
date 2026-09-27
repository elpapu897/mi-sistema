from pathlib import Path
import re
for fn in ['product','contact','refund']:
    s=Path('/tmp/gonvra_'+fn+'.html').read_text(errors='ignore')
    title=re.search(r'<title[^>]*>(.*?)</title>',s,re.I|re.S)
    print(fn,'bytes',len(s),'title',re.sub('<[^>]+>',' ',title.group(1)).strip() if title else '', '404_marker',len(re.findall('404',s,re.I)), 'PageView',len(re.findall('PageView',s,re.I)), 'ViewContent',len(re.findall('ViewContent',s,re.I)), 'pixel391',len(re.findall('3919766821491073',s)))
