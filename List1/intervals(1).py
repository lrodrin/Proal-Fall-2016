from jutge import read


def print_interval(a, b):
    print("[%d,%d]" % (a, b))

a1, b1, a2, b2 = read(int, int, int, int)
if a1 == a2 and b1 == b2:
    print_interval(a1, b1)
elif a2 < a1 and b1 <= b2:
    print_interval(a1, b1)
elif a2 <= a1 and b1 < b2:
    print_interval(a1, b1)
elif a1 < a2 and b2 <= b1:
    print_interval(a2, b2)
elif a1 <= a2 and b2 < b1:
    print_interval(a2, b2)
elif b1 < a2:
    print("[]")
elif b1 > a2 > a1:
    print_interval(a2, b1)
elif a2 < a1 < b2 < b1:
    print_interval(a1, b2)
elif b1 == a2:
    print_interval(b1, a2)
elif b2 == b1 and a1 < a2:
    print_interval(a2, b1)
elif b2 == b1 and a1 > a2:
    print_interval(a1, b1)
elif a1 == a2 and b1 < b2:
    print_interval(a1, b1)
elif a1 == a2 and b1 > b2:
    print_interval(a1, b2)
elif b2 < a1:
    print("[]")
elif b2 == a1:
    print_interval(a1, b2)
else:
    print("[]")
