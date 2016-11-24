from jutge import read

n = read(int)
seq = read(int)
pos = 1
while pos < n:
    seq = read(int)
    pos += 1
print("A la posicio %d hi ha un %d." % (n, seq))
