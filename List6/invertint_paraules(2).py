from jutge import read

n = read(int)
k = n
while k > 0:
    res = []
    word = read(str)
    for i in range(len(word)):
        res.append(word[i])
    print(''.join(reversed(res)))
    k -= 1

