# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math


def is_prime(x):
    assert isinstance(x, int)
    assert x > 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x%i == 0:
            return False
    else:
        return True


n = 600851475143
res = 0
for i in range(2, int(math.sqrt(n))):
    if is_prime(i) and n%i == 0:
        res = i
print(res)