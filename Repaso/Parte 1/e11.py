#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un 
# descuento del 60%. Escribir un programa que comience leyendo el número de barras 
# vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

def pan(num_barras):
    return "Precio habitual",(num_barras*3.49),"Descuento",(num_barras*3.49)-(num_barras*(3.49*0.6)),"Coste Final", (num_barras*(3.49*0.6))

print (pan(int(input("Ingrese numero de barras de pan \n"))))