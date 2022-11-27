def nombre_num(cadena,nombre,num):
    if(num==0):
        return cadena
    else:    
        return nombre_num(cadena+"\n"+nombre ,nombre ,num-1)

print(nombre_num("",input("Ingrese el nombre \n"),int(input("Ingrese el numero \n"))))
