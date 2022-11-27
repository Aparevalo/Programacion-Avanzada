def mayor_edad(edad):
    if(edad>18):
        return "Es mayor de edad"
    else:
        return "Es menor de edad"
print(mayor_edad(int(input("Ingrese su edad \n"))))