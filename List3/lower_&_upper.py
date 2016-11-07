def lowupp(cadena):
    cad_aux = ''
    if cadena[0] == '^':
        for i in range(1, len(cadena)):
            cad_aux = cad_aux + cadena[i].upper()
    elif cadena[0] == '_':
        for i in range(1, len(cadena)):
            cad_aux = cad_aux + cadena[i].lower()
    else:
        cad_aux = cadena
    return cad_aux
