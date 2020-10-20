from jutge import read

a = read(int)
c = []
while a is not None:
    c.append(a)
    a = read(int)

l2 = dict.fromkeys(c)

for a in c:
    l2[a] = c.count(a)

for k, v in l2.items():
    print("%s: %s" % (k, v))
