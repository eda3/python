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

# Measure the lap time
try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time, 2)
        total_time = round(now - start_time, 2)
        print('Lap #{}: {} ({})'.format(lap_num, total_time, lap_time), end='')
        lap_num += 1
        last_time = now  # Reset lap time
except KeyboardInterrupt:
    # Ctrl-C exceptions and suppress error messages
    print('\nEnd.')
