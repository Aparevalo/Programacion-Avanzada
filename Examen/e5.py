#Imprima los números del 1 al 10 al revés utilizando el ciclo for.

def imprimir(num):
    num=num+1
    for x in range(1,num):
        print(num-x)

imprimir(10)