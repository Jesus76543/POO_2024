from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="update clientes set direccion='Col. nueva vizcaya' where id=1"
    micursor.execute(sql)

    conexion.commit()
except:
    print(f"ocurrio un problema fasvor de verificar")
else:
    print("Registro actualizado correctamente")