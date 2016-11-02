from jutge import read

x = read(float)
x_pow = 1
total = 0

coef = read(float)
while coef is not None:
    total += coef * x_pow
    x_pow *= x
    coef = read(float)

print('{:.4f}'.format(total))
