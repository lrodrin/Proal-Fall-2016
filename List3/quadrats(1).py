from jutge import read


def Square1(n):
    for i in range(n):
        print(str(n) * n)


size = read(int)
if size is not None:
    Square1(size)
size = read(int)
while size is not None:
    print("")
    Square1(size)
    size = read(int)
