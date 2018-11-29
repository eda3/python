#! python3
# phoneAndEmail.py - クリップボードから電話番号とメアドを検索する

import pyperclip, re

phone_regrex = re.compile(r'''(
  (\d{3}|\(\d{3}\))? # 市街局番
  (\s|-|\.)? #区切り
  (\d{3}) #市内局番
  (\s|-|\.) #区切り
  (\d{4}) #加入者番号
  (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phone_regrex.findall(text):
  phone_num = '-'.join([groups[1], groups[3], groups[5]])
  print(phone_num)
