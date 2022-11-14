num1=int(input("Ingresar numero 1\n"))
num2=int(input("Ingresar numero 2\n"))
num3=int(input("Ingresar numero 3\n"))

if(num1>num2):
    pr3int(num1," es mayor a ",num2)
elif(num2>num1 and num3>num1 ) :
    print(num2," es mayor a ",num1)
    print(num3," es mayor a ",num1)
elif(num3>num1):
    print(num3," es mayor a ",num1)

