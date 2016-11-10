from jutge import read

a = read(chr)
i = 0
while a != '.':
    if a == 'a':
        i += 1
    a = read(chr)
print(i)
