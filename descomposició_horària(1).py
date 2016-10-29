from jutge import read

n = read(int)
h = n / 3600
n %= 3600
m = n / 60
n %= 60
s = n
print("%d %d %d" % (h, m, s))
