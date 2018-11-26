#! python3
# bulletPointAdder.py - クリップボードのテキストの各業に
# 点を打って、Wikipediaの箇条書きする

import pyperclip
text = pyperclip.paste()

# TODO： 業を分割して、'*'を追加する
lines = text.split('\n')
for i in range(len(lines)):  # "lines"リストの各要素をループ
  linex[i] = '* ' + lines[i] # "linesの要素に"* "を追加

pyperclip.copy(text)
