#! python3
# bulletPointAdder.py - クリップボードのテキストの各業に
# 点を打って、Wikipediaの箇条書きする

import pyperclip
text = pyperclip.paste()

# TODO： 業を分割して、'*'を追加する

pyperclip.copy(text)
