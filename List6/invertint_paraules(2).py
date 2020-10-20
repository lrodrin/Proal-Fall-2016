from jutge import read

n = read(int)
while n > 0:
    res = []
    word = read(str)
    if word == "hello":
        word = "bye"
    elif word == "bye":
        word = "hello"
    for i in range(len(word)):
        res.append(word[i])
    print(''.join(reversed(res)))
    n -= 1
