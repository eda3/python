#! python3
# mapIT.y - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser, sys, pyperclip

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if len(sys.argv) > 1:
  # コマンドラインから住所を取得
  address = ' '.join(sys.argv[1:])
  logger.debug('address:' + address)
else:
  # クリップボードから住所を取得する
  address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
