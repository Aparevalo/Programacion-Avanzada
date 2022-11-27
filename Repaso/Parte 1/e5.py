def sumar(numero,suma):
    if(numero==0):
        return suma
    else:    
        suma=suma+numero
        return sumar(numero-1, suma)

print(sumar(int(input("Ingrese un numero \n")),0))

