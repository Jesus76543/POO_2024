from conexionBD import *

class Clientes:
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def insertar(self):
        try:
            cursor.execute(
                "INSERT INTO clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)",
                (self.nif, self.nombre, self.direccion, self.ciudad, self.tel)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar cliente: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "SELECT * FROM clientes"
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar clientes: {e}")
            return None

    @staticmethod
    def actualizar(nif, nombre, direccion, ciudad, tel):
        try:
            cursor.execute(
                "UPDATE clientes SET nombre = %s, direccion = %s, ciudad = %s, tel = %s WHERE nif = %s",
                (nombre, direccion, ciudad, tel, nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False

    @staticmethod
    def eliminar(nif):
        try:
            cursor.execute(
                "DELETE FROM clientes WHERE nif = %s",
                (nif,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False
