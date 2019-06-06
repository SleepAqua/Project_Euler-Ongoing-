# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?

import time


start_time = time.time()

x = 2520**2
while True:
    for i in range(2, 21):
        if x%i != 0:
            x += 1
            break
    else:
        print(x)
        break
    
elapsed_time = time.time() - start_time
print(elapsed_time)