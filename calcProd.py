#! python3
import time


def calc_prod():
    # Obtain the product of 1 to 99,999
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


start_time = time.time()
prod = calc_prod()
end_time = time.time()
print('計算結果は{}桁です。'.format(len(str(prod))))
print('計算結果は{}秒でした。'.format(round(end_time - start_time, 2)))
