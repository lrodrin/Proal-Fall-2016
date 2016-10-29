from jutge import read

nom_1, nom_2 = read(str, str)
if nom_1 < nom_2:
    print(nom_1 + " < " + nom_2)
elif nom_1 > nom_2:
    print(nom_1 + " > " + nom_2)
else:
    print(nom_1 + " = " + nom_2)
