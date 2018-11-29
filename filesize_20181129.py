#! python3
import os

cwd = os.getcwd()
listdir = os.listdir('.')

total_size = 0
for filename in listdir:
  file_path = os.path.join(cwd, filename)
  print(file_path)

  total_size = total_size + os.path.getsize(file_path)

print(total_size)
