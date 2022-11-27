def fecha_na(fecha):
    fecha=fecha.split("/")
    return 'Día', fecha[0], 'Mes', fecha[1],'Año', fecha[2]

print(fecha_na(input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")))
