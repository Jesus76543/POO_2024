from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="delete from clientes where id=3"
    micursor.execute(sql)

    conexion.commit()
except:
    print(f"ocurrio un problema fasvor de verificar")
else:
    print("Registro eliminado registramente")   