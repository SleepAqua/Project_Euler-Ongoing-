# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

    
from Project_Euler_Q3 import is_prime
#exec(open("Project_Euler_Q3.py").read())

i = 0
p = 2
while i < 10001:
    if is_prime(p):
        i += 1
    p += 1
print(p - 1)