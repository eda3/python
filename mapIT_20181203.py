#! python3
# mapIT.y - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser, sys
if len(sys.argv) > 1:
  # コマンドラインから住所を取得
  address = ' '.join(sys.argv[1:])
