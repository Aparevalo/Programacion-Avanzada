#compuesto al año por 3 años
def interes(capital,cont):
    if(cont==3):
        return capital
    else:
        return interes(capital+(capital*0.04),cont+1)

print(interes(float(input("Ingrese el capital \n")),0))