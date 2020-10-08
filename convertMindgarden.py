# convertMindgarden.py
import json
import re
import codecs
from collections import OrderedDict

filepath = '/Users/Tadanori/dropbox/org/data.txt'
jsonfilepath = '/Users/Tadanori/dropbox/org/data.json'
       
with open(filepath) as f:
    l = f.readlines()

jsonbody = []
blockflag = False
body = ""
title = ""
for n in l:
    if n[0] == "#":
        if blockflag == False:
            title = n.rstrip('\n').replace('# ','')
            blockflag = True
        else:
            jsonbody.append(OrderedDict(title=title, body=body.rstrip()))
            body = ""
            blockflag == False
            title = n.rstrip('\n').replace('# ','')
    else:
        body = body + n    
else:
    if blockflag == True:
        jsonbody.append(OrderedDict(title=title, body=body.rstrip()))

with open(jsonfilepath, 'w', encoding='utf-8') as g:
    json.dump(jsonbody, g, indent=4,ensure_ascii=False)

    