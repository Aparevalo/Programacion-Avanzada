#3. Crear un ciclo for que cuente los números de 1 al 100.

def contar(cont,rango):
    if(rango==0):
        print (100)
    else:
        print(cont)
        return contar(cont+1,rango-1) 

contar(0,100)