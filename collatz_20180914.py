# coding:utf-8

# いい感じにコラッツ数列
def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


print('数字を入力してください：')
number = int(input())

while number != 1:
    number = collatz(number)
    print(str(number))

