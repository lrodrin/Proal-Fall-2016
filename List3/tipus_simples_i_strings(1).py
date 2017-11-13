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


# def slow_pi_aprox(n):
#     res = 0.
#     if n > 0:
#         for k in range(0, n):
#             e = (2 * k) + 1
#             res = (-1) ** (k / e)
#             res *= 4


def is_univariate_number(n):
    b = True
    n = str(n)
    for d in n:
        if d != n[0]:
            b = False
    return b


def is_invariate_word(s):
    b = True
    for c in s:
        if c.upper() != s[0].upper():
            b = False
    return b


drawH(5)
print(area_circle(2.5))
# print(slow_pi_aprox(50))
print(is_univariate_number(22322))
print(is_invariate_word("xxXxXXx"))
