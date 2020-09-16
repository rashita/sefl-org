# makelifehacknews.py

import sys
import datetime
import re

filepath = '/Users/Tadanori/dropbox/org/news.html'

if len(sys.argv) < 2:
    print(sys.argv[0])
    sys.exit()

with open(filepath) as f:
    l = f.readlines()

now = datetime.datetime.now()
todaydata = now.strftime('%Y年%m月%d日') 
s = re.sub('■あとで読む', todaydata, sys.argv[1])
s = s + '\n'
l.insert(20, s)
    
with open(filepath, mode='w') as f:
    f.writelines(l)