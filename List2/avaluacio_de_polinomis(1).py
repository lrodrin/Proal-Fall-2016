from jutge import read


def avalpoli(x, p):
    aval = 0.
    pot = 1.
    for i in range(0, len(p)):
        aval += p[i] * pot
        pot = pot * x
    return aval


if __name__ == "__main__":
    x = read(float)
    poli = read(float, float, float)
    print("%.4f" % (avalpoli(x, poli)))
