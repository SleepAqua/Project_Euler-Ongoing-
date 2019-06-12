#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?

x = str(2**1000)
r = 0
for i in range(len(x)):
    r += int(x[i])
print(r)