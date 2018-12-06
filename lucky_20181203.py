#! python3
# lucky.py - Google検索結果をいくつか開く

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a')
