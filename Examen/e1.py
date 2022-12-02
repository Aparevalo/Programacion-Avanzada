#Crear un script que indique si el usuario es mayor de edad, menor de edad o es parte de la tercera edad. 

def mayorEdad(edad):
    if(edad<18 and edad>0):
        return "Menor de Edad"
    elif(edad>=18 and edad<120):
        return "Mayor de Edada"
    else:
        return "Rango no valido"

print(mayorEdad(int(input("Ingrese una edad \n"))))
