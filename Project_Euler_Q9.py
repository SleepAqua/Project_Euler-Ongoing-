# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def is_Pythagorean_triplet(a, b, c):
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(c, int)
    assert 0 < a < b < c
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    

if __name__ == '__main__':
    def myfun():
        for a in range(1, 333):
            for b in range(2, 500):
                for c in range(335, 998):
                    if a < b < c:
                        if a + b + c == 1000 and is_Pythagorean_triplet(a, b, c):
                            return(a*b*c)
    print(myfun())
