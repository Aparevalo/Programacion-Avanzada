#Crear un bucle que cuente todos los números pares hasta el 100.

def contar(cont,rango):
    while rango>0:
        if(rango%2==0):
            cont=cont+1
            print(rango)
        rango=rango-1
    return "Son: "+str(cont)+" numeros pares" 
print(contar(0,100))