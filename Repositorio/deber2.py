def recorrer_lista(lista):
    for x in lista:
        print(x)

def agregar_lista(lista,rango):    
    if(rango==0):
        return lista
    else:
        num=int(input("Ingrese un numero \n"))
        lista.append(num)
        return(agregar_lista(lista,rango-1))


#Ejercicio 1: Define una función llamada menorque() que nos devuelva en pantalla el número 
# menor entre dos enteros. Define una salida de texto en caso de que.

def menorque(num1,num2):
    if(num1<num2):
        res=num1," Es el menor"
    else: 
        res=num2," Es el menor"
    return res
#print(menorque(15,9))

#Ejercicio 2: Define una función llamada num_max() que nos devuelva en pantalla el número
#mayor entre 4 diferentes enteros. No definas ningún valor a imprimir en caso
#de que ambos números sean iguales.

def num_max(lista):        
    mayor=lista[0]
    for x in range(1,len(lista)):
        if (lista[x]>mayor):
            mayor=lista[x]
    return(mayor)

lista=[]
#print(num_max(agregar_lista(lista,4)))

#Ejercicio 3: Define una función llamada num_max_min() que nos devuelva en pantalla el
#número mayor y menor entre 3 diferentes enteros. En caso de que todos sean
#iguales imprime en pantalla un mensaje indicándolo.

def num_max_min(lista):        
    inicio=lista[0]
    mayor=inicio
    menor=inicio
    for x in range(1,len(lista)):
        if (lista[x]>inicio):
            mayor=lista[x]
        else:
            menor=lista[x]
    return("El mayor",mayor," y el menor es ",menor)

#print(num_max_min(agregar_lista(lista,3)))

#Ejercicio 4: Define una función llamada num_max_min() que nos devuelva en pantalla el
#número mayor y menor entre 3 diferentes enteros. En caso de que todos sean
#iguales imprime en pantalla un mensaje indicándolo.

def num_max_min_ig(lista):        
    inicio=lista[0]
    mayor=inicio
    menor=inicio
    for x in range(1,len(lista)):
        if (lista[x]>inicio):
            mayor=lista[x]
        elif(lista[x]<inicio):
            menor=lista[x]
        else:
            return "Todos son iguales"
    return("El mayor",mayor," y el menor es ",menor)

#print(num_max_min_ig(agregar_lista(lista,3)))

#Ejercicio 5: Define una función que nos devuelva True si al darle una vocal mayúscula nos
# devuelva False, mientras que si es minúscula sea True.

def mayuscula_minuscula(vocal):
    if(vocal.lower() in  "aeiou"):
        if(vocal.isupper()):
            return True 
        else:
            return False    
    else:
        return "No es una vocal"
#print(mayuscula_minuscula(input("Ingrese una vocal \n")))

#Ejercicio 6: Define una función simple que no tenga parámetros y sólo imprima en pantalla un mensaje.

def mensaje():
    print("Hola mundo")

#Ejercicio 7: Define una función que permita imprimir un mensaje en base a los valores
#tomados de una lista para comprobar si todos los de la lista son mayores o menores de edad.


#Ejercicio 8: Define una función que permita multiplicar los números de una lista y sumar sus resultados.
def multiplicar(lista,sum,cont,rango):
    if(rango==0):
        return sum
    else:
        sum=sum*lista[cont]
        return multiplicar(lista,sum,cont+1,rango-1)
    
#print(multiplicar([2,4,5,6],1,0,4))    


#Ejercicio 9: Crea un código que solicite ingresar el nombre de un archivo con su extensión y
#devuelva la extensión de la misma. Por ejemplo: La extensión de programando-
#aprenderpython.py es “.py”
def extension(cadena):
    cad=cadena.split('.')
    return "La extension de: "+cad[0]+" es: "+cad[len(cad)-1]

print(extension(input("Ingrese nombre del archivo y su extension ")))