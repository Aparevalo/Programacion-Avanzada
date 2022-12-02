#Crear un bucle que sume los números del 100 al 200.

def sum(cont,inicio,rango):
    for x in range(inicio, rango):
        cont=cont+x
        #print(cont)
    return cont
print(sum(0,100,200))