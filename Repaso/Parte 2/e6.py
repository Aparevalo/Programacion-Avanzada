def cambiar_vocales(cadena,vocal):
    cadena1=""
    for letra in cadena:
        if letra.lower() in vocal.lower():
           letra=letra.upper()
        cadena1=cadena1+letra
    return cadena1

print(cambiar_vocales("Todo se puede con esfuerzo y ganas","ao"))