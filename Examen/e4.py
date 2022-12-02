#4. Haz una tabla de multiplicar utilizando el ciclo for.

def mult(base,limite):
    for x in range(0, (limite*base)+base, base):
        print(x) 

mult(int(input("Ingrese la base\n")),int(input("Ingrese el limite\n")))
