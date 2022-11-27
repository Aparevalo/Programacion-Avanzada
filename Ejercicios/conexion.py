import pymysql.cursors

def conexion(servidor,usuario,contra,base_datos):
    connection = pymysql.connect(host=servidor,
                                user=usuario,
                                password=contra,
                                database=base_datos,
                                cursorclass=pymysql.cursors.DictCursor)
    return connection