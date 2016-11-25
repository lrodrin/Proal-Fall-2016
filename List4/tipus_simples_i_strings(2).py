def um_count(s):
    cont = 0
    for word in s.split():
        if "um" in word:
            cont += 1
    return cont


def word_count(s):
    cont = 0
    for word in s.split():
        if word in s:
            cont += 1
    return cont


def kth_word(s, k):
    if k >= 1:
        cont = 1
        for word in s.split():
            if cont == k:
                return word
            cont += 1


def suc_word(s):
    for word in s.split():
        for c in word:
            if c.isupper():
                return word


def drawA(n):
    pass


print(um_count("Qui iumnvenit amicum invenit thumesauruM"))
print(word_count("Alea iacta          est            hehe"))
print(kth_word("Alea iacta est", 2))
print(suc_word("qui invenit amicum iNvenit thesauruM"))
drawA(5)
