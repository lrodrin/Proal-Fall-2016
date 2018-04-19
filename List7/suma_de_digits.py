from jutge import read

n = read(int)
while n is not None:
    if 0 <= n <= 9:
        print("La suma dels digits de %d es %d." % (n, n))
    else:
        print("La suma dels digits de %d es " % n, end="")
        suma = 0
        for i in str(n):
            suma += int(i)
        print("%d." % suma)
    n = read(int)
