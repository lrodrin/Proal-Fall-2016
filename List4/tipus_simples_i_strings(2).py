def um_count(s):
    subs = "um"
    return s.count(subs, 0, len(s))


def word_count(s):
    cont = 0
    for _ in s.split():
        cont += 1
    return cont


def kth_word(s, k):
    if k >= 1:
        if k <= len(s.split()):
            word = s.split()
            return word[k - 1]
        else:
            return ""


def suc_word(s):
    result = ""
    for word in s.split():
        for c in word:
            if c.isupper():
                result = word
                break
        else:
            continue
        break
    return result


def drawA(n):
    print(" " * (n - 1) + "*")
    j = n
    for i in reversed(range(n - 1)):
        if i == n - 2:
            print(" " * i + "* *")
        elif i == n - 3:
            print(" " * i + "*" * n)
        else:
            print(" " * i + "*" + " " * j + "*")
            j += 2


print(um_count("Qui invenit amicum invenit thesauruM"))
print(word_count("Alea iacta          est"))
print(kth_word("Alea iacta est", 3))
print(suc_word("qui invenit amiCum invenit thesauruM"))
drawA(5)
