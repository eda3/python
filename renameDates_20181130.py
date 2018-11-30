#! python3
# renameDates.py - 米国式日付MM-DD-YYYYのファイル名を欧州式DD-MM-YYYYに書き換える

import shutil, os, re

# 米国式日付のファイル名にマッチする正規表現を作る
date_pattern = re.compile(r"""
    ^(.*?)          # 日付の前の全テキスト
    ((0|1)?\d)-     # 月を表す1,2桁の数字
    ((0|1|2|3)?\d)- # 日を表す1,2桁の数字
    ((19|20)\d\d)   # 年を表す4桁の数字
    (.*?)$          # 日付の後の全テキスト
    """, re.VERBOSE)

# カレントディレクトリの全ファイルをループする
for amer_filename in os.listdir('.'):
  mo = date_pattern.search(amer_filename)

# 日付のないファイルをスキップする

# ファイル名を部分分解する

# 欧州式の日付のファイル名を作る

# ファイル名を変更する
