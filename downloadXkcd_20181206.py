#! python3
# downloadXkcd.py - XKCDコミックを一つずつダウンロードする

import requests, os, bs4
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
  # ページをダウンロードする
  print('ページをダウンロード中 {}...'.format(url))
  res = requests.get(url)
  res.raise_for_status()

  soup = bs4.BeautifulSoup(res.text)
