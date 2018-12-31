#! python3
# quickWeather.py - コマンドラインに指定した地名の天気予報を表示する
import sys
import requests
import json
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
