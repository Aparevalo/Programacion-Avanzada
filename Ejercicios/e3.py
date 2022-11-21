def calificacion(nota):
    if(nota<=10 and nota>=9):
        valor="Excelente"
    elif(nota<9 and nota>=8):
        valor="Muy Bueno"
    elif(nota<8 and nota>=7):
        valor="Bueno"
    elif(nota<7 and nota>=0):
        valor="Reprobado"
    else:
        valor="Valor desconocido"

    return valor

print(calificacion(float(input("Ingrese la nota \n"))))