def um_count(s):
    cont = 0
    for i in range(len(s)):
        if s[i] == 'u' and s[i + 1] == 'm':
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
        res = ""
        for word in s.split():
            if cont == k:
                return word
            cont +=1

def suc_word(n):
    pass


def drawA(n):
    pass


print(um_count("Qui invenit amicum invenit thesauruM"))
print(word_count("Alea iacta          est"))
print(kth_word("Alea iacta est", 3))
suc_word("qui invenit amiCum invenit thesauruM")
drawA(5)
