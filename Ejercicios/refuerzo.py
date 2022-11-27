#Refuerzo para la prueba
#1





def operacion():
    return  (3+ pow(2,2))/2.5


while True:
    op = int(input("Ingresa numero ejercicio: o 0 para salir \n"))
    if (op == 0):
        break
    elif (op == 1): 
        print(saludar())
    elif (op == 2): 
        print(saludar2())
    elif (op == 3): 
        print(nombre(input("Ingresa numero ejercicio: o 0 para salir \n")))
    elif (op == 4): 
        print(operacion())
    
    