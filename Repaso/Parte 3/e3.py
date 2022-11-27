def dividir(num1,num2):
    if(num2==0):
        return "Error"
    else:
        return num1/num2

print(dividir(int(input("Ingrese dividendo\n")),int(input("Ingrese dividendo\n"))))