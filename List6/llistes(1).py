def cerca(val, llista, i, j):
    return i <= j and val in llista[i: j + 1]


def count_diff(f):
    counter = 0
    n = len(f)
    for k in range(n):
        if not cerca(f[k], f, 0, k - 1):
            counter += 1
    return counter


def product(u, v):
    n = len(u)
    res = 0.
    for k in range(n):
        res += u[k] * v[k]
    return res


def delete_multiples(k, f):
    result_list = []
    for num in f:
        if num % k != 0:
            result_list.append(num)
    return result_list


def erato(n):
    multiples = []
    result_list = []
    for i in range(2, n + 1):
        if i not in multiples:
            result_list.append(i)
            for j in range(i * i, n + 1, i):
                multiples.append(j)
    return result_list


def merge(f, g):
    i, j = 0, 0
    result_list = []
    while i < len(f) and j < len(g):
        if f[i] <= g[j]:
            result_list.append(f[i])
            i += 1
        else:
            result_list.append(g[j])
            j += 1

    while j < len(g):
        result_list.append(g[j])
        j += 1
    while i < len(f):
        result_list.append(f[i])
        i += 1
    return result_list
