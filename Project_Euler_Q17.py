'''If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance with
British usage.'''

def englize(n):
    assert 0 <= n <= 1000
    assert isinstance(n, int)
    lv1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
       "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
       "sixteen", "seventeen", "eighteen", "nineteen"]
    lv2 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
           "eighty", "ninety"]
    if n < 20:
        return lv1[n]
    elif 20 <= n < 100:
        return lv2[n//10] + (lv1[n%10] if n%10 != 0 else "")
    elif 100 <= n < 1000:
        return lv1[n//100] + "hundred" + ("and" + englize(n%100) if (n % 100 != 0) else "")
    elif n == 1000:
        return "one" + "thousand"

if __name__ == "__main__":
    res = 0
    for i in range(1, 1001):
        res += len(englize(i))
    print(res)