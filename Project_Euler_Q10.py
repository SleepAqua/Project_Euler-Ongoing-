# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


from Project_Euler_Q3 import is_prime


res = 0
for i in range(2, 2000000):
    if is_prime(i):
        res += i
print(res)