#Ejercicio 1: Multiplicar 2 números sin usar el símbolo de la multiplicación
#num1 = int(input("Ingrese numero 1 \n"))
#num2 = int(input("Ingrese numero 2 \n"))
def multiplicar(num1,num2):
    sum=0
    cont=0
    while(cont<num2):
        sum=sum+num1
        cont+=1
    return(sum)

#print(multiplicar(3,4))

#Ejercicio 2: Ingresar nombre y apellido e imprimirlo al revés.


def invertir_cadena(cadena):
    return cadena[::-1]

#print(invertir_cadena("Anderson Arevalo"))

#Ejercicio 3: Crear un script que encuentre el elemento menor de una lista

def elemento_menor(lista):
    menor=lista[0]
    for x in range(1,len(lista)):
        if (lista[x]<menor):
            menor=lista[x]
    return(menor)
lista=[2,3,6,-8,1,7]
#print(elemento_menor(lista))

#Ejercicio 4: Crear un script que imprima el volumen de una esfera por su radio

def volumen_esfera(radio):
    return ((4/3)*3.14*pow(radio,3))
#print (volumen_esfera(4))

#Ejercicio 5:Crear una script que indique si el usuario es mayor de edad

def mayor_edad(edad):
    if(edad>=18):
        imp="mayor edad"
    else:
        imp="menor de edad"
    return imp

#print(mayor_edad(25))

#Ejercicio 6:Crear un script que permita calcular si un número es par o impar

def par_impar(num):
    if(num%2==0):
        imp="par"
    else:
        imp="impar"
    return imp
#print(par_impar(10))

#Ejercicio 7: Crear un script que indique cuantas vocales tiene una palabra

def contar_vocales(cadena):
	cont = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			cont += 1
	return cont
#print(contar_vocales("MURcielaGO")) 

#Ejercicio 8: Crear un script que reciba una cantidad infinita de números hasta decir basta, luego que imprima la suma de los números ingresados.

def inf_parar(sum):
    num = input("Ingrese stop para parar, sino ingrese un numero \n")
    if(num == "stop"):
        return int(sum)
    else:
        return inf_parar(int(sum)+int(num))
#print(inf_parar(0))

#Ejercicio 9:  crear un sistema de calificaciones
def calificacion(nota):
    if(nota==10 or nota>=9):
        valor="A"
    elif(nota<9 and nota>=8):
        valor="B"
    elif(nota<8 and nota>=7):
        valor="C"
    elif(nota<7 and nota>=6):
        valor="D"
    elif(nota<6 and nota>=0):
        valor="F"
    else:
        valor="Valor desconocido"

    return valor

#print(calificacion(7.5))

# Ejercicio 10: Imprimir números de 5 a 1 de manera descendente

def num_des(num,cadena):
    if(num==0):
        return cadena
    else:
        return num_des(num-1,cadena+str(num)+"\n")
#print(num_des(5,""))

# Ejercicio 11:Imprimir los números naturales del 0 al 10 utilizando un ciclo while

def num_while(num):
    cont=0
    while(cont<=num):
        print(cont)
        cont+=1

#num_while(10)

#Ejercicio 12: Calcular el área y el perímetro de un Rectángulo

def area_perimetro(alto,ancho):
    return "Area = ",(int(alto)*int(ancho)),"Perimetro = ",(int(alto)+int(ancho))
#print(area_perimetro(12,45))

#Ejercicio 13: terar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3

def num_div_tres(rango):
    for x in range(1,rango):
        if(x%3==0):
            print(x)  

#num_div_tres(11)

#Ejercicio 14:Presentar un string con el titulo y el autor de un libro

def presentar(titulo,autor):
    return "Titulo: "+titulo+" Autor: "+autor
#print(presentar("Cronicas de una muerte anunciada","Gabriel Garcia Marquez")) 


#Ejercicio 15: Se debe imprimir el mayor de los dos números
def mayor():
    num1 = int(input("Proporciona el numero 1 \n"))
    num2 = int(input("Proporciona el numero 2 \n"))
    if(num1>num2):
        return "El numero mayor es ",num1
    else:
        return "El numero mayor es ",num2
#print(mayor())
#Ejercicio 16: Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for

#Ejercicio 17: Crear un script que encuentre la potencia de un número ingresado por el teclado
def potencia():
    num1 = int(input("Proporciona un numero \n"))
    num2 = int(input("Proporciona la potencia \n"))
    return pow(num1,num2)
#print(potencia()) 

#Ejercicio 18: Dado dos números enteros, encontrar la suma

def suma(num1,num2):
    return num1+num2
#print(suma(4,7))


#Ejercicio 19: Dado un número de 5 dígitos, devolver el número en orden inverso.
def invertir_numero(num):
    return str(num)[::-1]
#print(invertir_numero(12345))


#Ejercicio 20: Crear un script para saludar desde Python
def saludar():
    return "hola mundo"
#print(saludar())

  
        
        
        


        

        

