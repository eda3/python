#! python3
# stopwatch.py simpl stopwatch

import time

# Display program description
print('Press Enter to start.')
print('After that, display the elapsed time by pressing Enter.')
print('Press Ctrl-C to exit')
input()  # Press Enter to start
print('Start')
start_time = time.time()  # Program and start timeof first lap
last_time = start_time
lap_num = 1
