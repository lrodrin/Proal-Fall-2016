from jutge import read

n = read(int)
if n < 10:
    print("fa fred")
    if n <= 0: print("l'aigua es gelaria")
elif n > 30:
    print("fa calor")
    if n >= 100: print("l'aigua bulliria")
else:
    print("s'esta be")
