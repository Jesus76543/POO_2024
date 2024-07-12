from conexionBD import *
try:
    micursor=conexion.cursor()
    nombre=input("¿Cual es el nombre?")
    direccion=input("¿Cual es tu direccion?")
    tel=input("¿Cual es tu numero de telefono?")
    
    sql="insert into clientes (id,nombre,direccion,tel) values (null,%s,%s,%s)"
    valores=(nombre,direccion,tel)
    micursor.execute(sql)

#Sirve para finalizar la ejecucion del SQL
    conexion.commit()
except:
    print(f"ocurrio un problema favor de verificar")
else:
    print(f"Registro  insertado Exitosamente")
    