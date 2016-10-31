from jutge import read

n, m = read(int, int)
if n == m:
    print(n)
elif n < m:
    for i in range(n, m + 1):
        if i != m:
            print(i, end=",")
        else:
            print(m)
else:
    print()