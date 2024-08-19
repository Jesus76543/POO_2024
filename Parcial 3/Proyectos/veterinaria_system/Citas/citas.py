from conexionBD import conectar

def agendar_cita():
    conexion = conectar()
    cursor = conexion.cursor()
    
    ficha = input("Ficha: ")
    id_cliente = input("ID del Cliente: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    descripcion = input("Descripción: ")
    
    try:
        cursor.execute('''
        INSERT INTO Cita (Ficha, Cliente, Fecha, Descripcion)
        VALUES (%s, %s, %s, %s)
        ''', (ficha, id_cliente, fecha, descripcion))
        
        conexion.commit()
        print("Cita agendada exitosamente")
    except Exception as e:
        print(f"Error al agendar la cita: {e}")
    finally:
        conexion.close()

def modificar_cita():
    conexion = conectar()
    cursor = conexion.cursor()
    
    id_cita = input("ID de la Cita a modificar: ")
    nueva_ficha = input("Nueva Ficha: ")
    nuevo_cliente = input("Nuevo ID del Cliente: ")
    nueva_fecha = input("Nueva Fecha (YYYY-MM-DD): ")
    nueva_descripcion = input("Nueva Descripción: ")
    
    try:
        cursor.execute('''
        UPDATE Cita
        SET Ficha = %s, Cliente = %s, Fecha = %s, Descripcion = %s
        WHERE idCita = %s
        ''', (nueva_ficha, nuevo_cliente, nueva_fecha, nueva_descripcion, id_cita))
        
        conexion.commit()
        print("Cita modificada exitosamente")
    except Exception as e:
        print(f"Error al modificar la cita: {e}")
    finally:
        conexion.close()

def eliminar_cita():
    conexion = conectar()
    cursor = conexion.cursor()
    
    id_cita = input("ID de la Cita a eliminar: ")
    
    try:
        cursor.execute('''
        DELETE FROM Cita WHERE idCita = %s
        ''', (id_cita,))
        
        conexion.commit()
        print("Cita eliminada exitosamente")
    except Exception as e:
        print(f"Error al eliminar la cita: {e}")
    finally:
        conexion.close()
