from Clientes import clientes
from Empleados import empleados
from Citas import citas

def menu_principal():
    while True:
        print("Menú Principal")
        print("1. Clientes")
        print("2. Empleados")
        print("3. Citas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_empleados()
        elif opcion == '3':
            menu_citas()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

def menu_clientes():
    while True:
        print("Menú Clientes")
        print("1. Registrar Cliente")
        print("2. Eliminar Cliente")
        print("3. Modificar Cliente")
        print("4. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            clientes.registrar_cliente()
        elif opcion == '2':
            clientes.eliminar_cliente()
        elif opcion == '3':
            clientes.modificar_cliente()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

def menu_empleados():
    while True:
        print("Menú Empleados")
        print("1. Registrar Empleado")
        print("2. Eliminar Empleado")
        print("3. Modificar Empleado")
        print("4. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            empleados.registrar_empleado()
        elif opcion == '2':
            empleados.eliminar_empleado()
        elif opcion == '3':
            empleados.modificar_empleado()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

def menu_citas():
    while True:
        print("Menú Citas")
        print("1. Agendar Cita")
        print("2. Modificar Cita")
        print("3. Eliminar Cita")
        print("4. Regresar al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            citas.agendar_cita()
        elif opcion == '2':
            citas.modificar_cita()
        elif opcion == '3':
            citas.eliminar_cita()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu_principal()
