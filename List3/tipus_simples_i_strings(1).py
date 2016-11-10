import math


def drawH(n):
    if n % 2 != 0 and n >= 3:
        for i in range(n):
            if n // 2 == i:
                print("*" * n)
            else:
                print("*   *")


def area_circle(r):
    if r >= 0:
        r *= r
        r *= math.pi
        return "%.2f" % r


def slow_pi_aprox(n):
    res = 0.
    if n > 0:
        for k in range(0, n):
            e = (2 * k) + 1
            res = (-1) ** (k / e)
            res *= 4


def is_invariate_word(s):
    b = False
    for c in range(len(s)-1):
        if s[c] == s[c+1]:
            b = True
    return b

drawH(5)
print(area_circle(2.5))
#print(slow_pi_aprox(50))
print(is_invariate_word("xxXxXXy"))