#dashboad.py
import webbrowser
import os
import re
import markdown

#IDAE:日付や曜日を表示する？ javascript
#ローカルサーバーで開く？→個別ファイルへの書き出しができるかも
#TODO:DIVを横並びにするrow/colum→header.html
#表示行数を限定する/スクロール表示にする
#TODO:htmlにファビコンをつける

path_temphaader = "material/header.html"
path_tempfooter = "material/footer.html"
path_output = "material/index.html"
#TODO:関数で特定のフォルダからファイルを読んで配列にして保持するようにする
path_loadfile = ["これから書くこと.md","todo.txt","書籍の企画案.md","書きたいこと・エッセイ.md","気をつけたいこと.md","曜日別アウトプット.md"]

with open(path_temphaader) as f1:
     tempHead = f1.read()
with open(path_tempfooter) as f2:
     tempFoot = f2.read()

#ファイルを読み込んで中身を返す
#TODO:三つ読み込んだら、rowを切り替える処理
def loadfile(path):
     with open(path) as f:
          arr = f.readlines()
     return arr

#配列の一行目をヘッダーにそれ以降を中身にして返す
#MEMO:idの処理が必要？
def divalse(arr):
     tempHeader = re.sub(r'^#','',arr[0]).strip()
     tmpBody = ''.join(arr[1:10]) #ページ内容を読み込む範囲
     md = markdown.Markdown(extensions=['markdown_checklist.extension'])
     tmpBody = md.convert(tmpBody)

     writinglistHeader = '<h2 class="contentHeader">' + tempHeader + '</h2>'
     writinglistBody = '<div class="contentBody">' + tmpBody + '</div>'
     
     return '<div class="col-4">' + writinglistHeader + writinglistBody + '</div>'

### 以下の処理がダサイ
m = ""

for n in range(len(path_loadfile)):
     if (n == 0) or (n % 3 == 0):
          m = m +  '<div class="row">'
     m = m + divalse(loadfile(path_loadfile[n]))
     if ((n + 1) % 3 == 0) or n == len(path_loadfile):
          m = m + '</div>'

htmlbody = tempHead +m + tempFoot
with open(path_output, mode='w') as f:
     f.write(htmlbody)

webbrowser.open('file://' + os.path.realpath(path_output))