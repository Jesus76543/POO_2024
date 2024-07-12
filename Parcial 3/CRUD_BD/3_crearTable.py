from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="create table clientes1(id int primary key auto_increment, nombre varchar(60), direccion varchar(120), tel varchar(10))"

    micursor.execute(sql)

    if micursor:
        print(f"Se creo la tabla Exitosamnete")
        
except:
    print(f"SE MURIOOOOOO")
    
else:
    print(f"Se creo correctamente :D")