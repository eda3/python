#!python3

import threading
import time

print('Program start')


def take_a_nap():
    time.sleep(5)
    print('woke up!')


thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print('Program end')
