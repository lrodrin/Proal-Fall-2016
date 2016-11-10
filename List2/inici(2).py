def vowel_consonant(s):
    compt_v = 0
    compt_c = 0
    if len(s) != 0:
        for c in s:
            if c.islower():
                if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                    compt_v += 1
                else:
                    compt_c += 1
            else:
                if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                    compt_v += 1
                else:
                    compt_c += 1
        return "(%d, %d)" % (compt_v, compt_c)


def delete_digits(s):
    res = []
    if len(s) != 0:
        for i in range(len(s)):
            if not s[i].isdigit():
                res.append(s[i])
        return ''.join(res)


def switch(s):
    res = []
    if len(s) != 0:
        for i in range(len(s)):
            if s[i].isupper():
                res.append(s[i].lower())
            else:
                res.append(s[i].upper())
        return ''.join(res)


def countdown(n):
    if n > 0:
        for i in reversed(range(n + 1)):
            if i == 0:
                print(i)
            else:
                print(i, end=" ")


def powers_of_2(n):
    if n >= 1:
        for i in range(0, n):
            if i == n-1:
                print(2 ** i)
            else:
                print(2 ** i, end=" ")