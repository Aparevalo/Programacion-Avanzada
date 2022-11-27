#Escribir un programa que pregunte el nombre completo del usuario en la 
# consola y después muestre por pantalla el nombre completo del usuario tres veces, 
# una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera 
# letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas 
# y minúsculas como quiera.

def nombre_con(nombre):
    n=""   
    nombre1=nombre.split(' ')
    for x  in nombre1:
       n= n+ x.lower().capitalize()+" " 
    cadena=nombre.lower()+"\n"+nombre.upper()+"\n"+n
    return cadena  

print(nombre_con("anderson arevalo"))




