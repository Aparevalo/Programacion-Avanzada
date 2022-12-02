#Realizar un programa que enumere los países de la siguiente lista: 
# countries = ["Ecuador", "Perú", "Estados Unidos", "España"]

def enumerar(lista):
    for x in range(0,len(lista)):
        print(str(x+1)+": "+lista[x])

countries = ["Ecuador", "Perú", "Estados Unidos", "España"]

enumerar(countries) 