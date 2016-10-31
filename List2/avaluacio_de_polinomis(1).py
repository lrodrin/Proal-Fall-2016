from jutge import read


def avalpoli(x, P):
    aval = 0.
    pot = 1.
    for i in range(0, len(P)):
        aval += P[i] * pot
        pot = pot * x
    return aval


if __name__ == "__main__":
    x = read(float)
    polinomi = read(float)
    print(avalpoli(x, polinomi))
