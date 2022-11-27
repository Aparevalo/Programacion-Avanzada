guardada="default"
def inicar_contra(contra,guardada):
    if(contra.lower()==guardada.lower()):
        return "Contraseña correcta"
    else:
        return "Contraseñas no coinciden"

while True:
    op = int(input("Ingresa 1 para agregar o cambiar contraseña \nIngrese 2 para comprobar contraseña\nIngrese 0 para salir\n"))
    if (op == 0):
        break
    elif(op==1):
        guardada=input("Ingrese contraseña a guardar: ")
    elif(op==2):
        contra=input("Ingrese contraseña: ")
        print(inicar_contra(contra,guardada))
