import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )

except:
    print("Se ha producido un error con el servidor, verifique mais tarde")
    
else:
        #Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    micursor=conexion.cursor()

    sql="create database bd_python1"
    #Ejecutar la consulta sql
    micursor.execute(sql)

    if micursor:
        print(f"Se creo la BD exitosamente")
    #Mostrar las BD que existen en el SGBD Mysql
    micursor.execute("show database")

    for x in micursor:
        print(x)