def interes(capital,interes,anios):
    return (capital*(interes/100))*anios

print(interes(float(input("Ingrese el capital \n")),float(input("Ingrese el interes \n")),int(input("Ingrese los años \n"))))
