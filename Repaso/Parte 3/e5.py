def tributar(edad,ingresos):
    if edad > 16 and ingresos >= 1000:
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")

tributar(int(input("¿Cuál es tu edad? ")),float(input("¿Cuales son tus ingresos mensuales? ")))
