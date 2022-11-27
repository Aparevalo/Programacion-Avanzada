from conexion import conexion
    
conectar=conexion("localhost","root","","informatica")

with conectar:
    with conectar.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
print ("Database version : {0}".format(data))