#dashboad.py
import webbrowser
import os
import markdown

#IDAE:日付や曜日を表示する？ javascript
#ローカルサーバーで開く？→個別ファイルへの書き出しができるかも
#DIVを横並びにするrow/colum
#表示行数を限定する/スクロール表示にする

path_temphaader = "material/header.html"
path_tempfooter = "material/footer.html"
path_output = "material/index.html"
#読み込むファイルのリストを配列で持つ？
path_writinglist = "これから書くこと.md" 
path_todolist = "todo.txt"

with open(path_temphaader) as f1:
     tempHead = f1.read()
with open(path_tempfooter) as f2:
     tempFoot = f2.read()

with open(path_writinglist) as fa:
     arrA = fa.readlines()
with open(path_todolist) as fb:
     arrB = fb.readlines()

#TODO: 以下の処理の関数化
tmpBodyA = ''.join(arrA[1:])
md = markdown.Markdown(extensions=['markdown_checklist.extension'])
tmpBodyA = md.convert(tmpBodyA)

tmpBodyB = ''.join(arrB[1:])
md = markdown.Markdown(extensions=['markdown_checklist.extension'])
tmpBodyB = md.convert(tmpBodyB)

## TODO:置換して頭のハッシュを取る
## TODO:前後の空白を取る
writinglistHeader = '<h3 class="contentHeader">' + arrA[0] + '</h3>'
writinglistBody = '<div class="contentBody">' + tmpBodyA + '</div>'

todolistHeader = '<h3 class="contentHeader">' + arrB[0] + '</h3>'
todolistBody = '<div class="contentBody">' + tmpBodyB + '</div>'

htmlbody = tempHead +writinglistHeader +  writinglistBody + todolistHeader + todolistBody + tempFoot
with open(path_output, mode='w') as f:
     f.write(htmlbody)

webbrowser.open('file://' + os.path.realpath(path_output))