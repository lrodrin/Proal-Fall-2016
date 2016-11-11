from jutge import read

word = read(str)
while word is not None:
    res = []
    for i in range(len(word)):
        res.append(word[i])
    print(''.join(reversed(res)))
    word = read(str)
