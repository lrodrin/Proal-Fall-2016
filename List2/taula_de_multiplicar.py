from jutge import read

n = read(int)
for i in range(1, 11):
    print("%d*%d = %d" % (n, i, n*i))
