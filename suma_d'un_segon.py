from jutge import read

h, m, s = read(int, int, int)
s += 1

if s >= 60:
    s = 0
    m += 1
if m >= 60:
    m = 0
    h += 1
if h >= 24: h = 0

if h < 10: print("0", end="")
print("%d:" % h, end="")
if m < 10: print("0", end="")
print("%d:" % m, end="")
if s < 10: print("0", end="")
print(s)
