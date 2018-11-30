#! python3
# mcb.pyw - クリップボードの保存・復元
# Usage:
#   py.exe mcb.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
#   py.exe mcb.pyw <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
#   py.exe mcb.pyw list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys

mcb_shelve = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
  print('save')
  mcb_shelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
  # キーワード一覧と、内容の読み込み

mcb_shelve.close()
