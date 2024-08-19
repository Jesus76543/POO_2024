from conexionBD import *

class Revision:
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula

    def insertar(self):
        try:
            cursor.execute(
                "INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar revision: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM revisiones")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar revisiones: {e}")
            return None

    @staticmethod
    def actualizar(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        try:
            cursor.execute(
                "UPDATE revisiones SET cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s, matricula = %s WHERE no_revision = %s",
                (cambiofiltro, cambioaceite, cambiofrenos, otros, matricula, no_revision)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar revision: {e}")
            return False

    @staticmethod
    def eliminar(no_revision):
        try:
            cursor.execute(
                "DELETE FROM revisiones WHERE no_revision = %s",
                (no_revision,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar revision: {e}")
            return False
