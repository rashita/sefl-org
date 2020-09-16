# enbranch.py

import sys
import datetime
import re
from bs4 import BeautifulSoup
import writelog

filepath = '/Users/Tadanori/dropbox/org/temp.txt'
newsfilepath = '/Users/Tadanori/dropbox/org/news.html'

now = datetime.datetime.now()
todaydata = now.strftime('%Y年%m月%d日') 

if len(sys.argv) < 3:
    sys.exit()

html = sys.argv[1]
maxnumber = sys.argv[2]

def setBranch(html,pattern,filename):
    results = re.findall(pattern, html, re.S)
    tbody = ''.join(results)
    with open(filename) as f:
        l = f.readlines()
    s = tbody.replace('■あとで読む',todaydata, ).replace('<h3','<h2').replace('/h3>','/h2>')
    s = s + '\n'
    l.insert(20, s)

    with open(filename, mode='w') as f:
        f.writelines(l)

#<h3 style="border-bottom:1.5px solid #999">■あとで読む</h3>
#あとで読むの処理
setBranch(html,'(<h3 style="border-bottom:1.5px solid #999">■あとで読む</h3>.*?)</td>',newsfilepath)

#アイデアノートの処理
pattern = '<tr>[\\s\\S]*?<td[\\s\\S]*?(<h4.[\\s\\S]*?)</td>[\\s\\S]*?</tr>'
results = re.findall(pattern, html, re.S)

tempbody = ""
for n in reversed(results):
    setnumber =  re.findall(r'<h4.*?>(\d+).*?</h4>',n, re.S)
    for i in setnumber:
        if int(i) > int(maxnumber):
            maxnumber = int(i)
    soup = BeautifulSoup(n.replace('</h4>','</h4>\n') ,"html.parser")
    tempbody = tempbody + '# ' + soup.get_text() + '\n'
writelog.writelog(tempbody, '/Users/Tadanori/dropbox/org/data.txt')

#プロジェクトノートの処理
tempbody = todaydata + '\n\n'
pattern = '(<h3 style="border-bottom:1.5px solid #999">project: .*?)</td>'
results = re.findall(pattern, html, re.S)
for n in results:
    soup = BeautifulSoup(n.replace('</h3>','</h3>\n') .replace('project:','') ,"html.parser")
    tempbody = tempbody + '## ' + soup.get_text() + '\n'
writelog.writelog(tempbody, '/Users/Tadanori/dropbox/org/projectlog.txt')

#断片的執筆の処理
tempbody=""
pattern = '(<h3 style="border-bottom:1.5px solid #999">fragment: .*?)</td>'
results = re.findall(pattern, html, re.S)
for n in results:
    soup = BeautifulSoup(n.replace('</h3>','</h3>\n') .replace('fragment:',''),"html.parser")
    tempbody = tempbody + '# ' + soup.get_text() + '\n'
writelog.writelog(tempbody, '/Users/Tadanori/dropbox/org/fragmentitem.txt')

#ブックノートの処理
tempbody=""
pattern = '(<h3 style="border-bottom:1.5px solid #999">book: .*?)</td>'
results = re.findall(pattern, html, re.S)
for n in results:
    soup = BeautifulSoup(n.replace('</h3>','</h3>\n') .replace('book:',''),"html.parser")
    tempbody = tempbody + '# ' + soup.get_text() + '\n'
writelog.writelog(tempbody, '/Users/Tadanori/dropbox/org/booklog.txt')

#ノーブランチの処理はしない

if __name__ == '__main__':
    #sys.stdout.write(maxnumber)
    print(maxnumber) 