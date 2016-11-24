from jutge import read

n = read(int)
while n is not None:
    if 0 <= n <= 9:
        print("El producte dels digits de %d es %d." % (n, n))
    else:
        print("El producte dels digits de %d es " % n, end="")
        prod = 1
        for i in str(n):
            prod *= int(i)
        print("%d." % prod)
    n = read(int)
print("----------")
