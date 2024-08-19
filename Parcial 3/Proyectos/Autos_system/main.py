from revisiones import Revisiones
from clientes import Clientes
from autos import Autos
import getpass
from Funciones import * 
from usuarios import Usuarios

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registrarse
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ")
        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            #Agregar codigo
            obj_usuario=Usuarios.Usuario(nombre,apellidos,email,password)
            resultado=obj_usuario.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos} se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")    
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Agregar codigo   
            # obj_usuario=usuario.Usuario("","",email,password)
            registro=Usuarios.Usuario.iniciar_sesion(email,password)
            if registro:
               menu_secundario()
            else:
               print(f"\n\t ** Nombre de usuario y/o contraseña incorrectos, intentalo de nuevo ** ...")
               esperarTecla()          
        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()


def menu_secundario():
    while True:
        borrarPantalla()
        print("""
      .::  Menu AGENCIA AUTOS ::. 
          1.- Revisiones
          2.- Clientes
          3.- Autos
          4.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            menu_revisiones()
        elif opcion == '2':
            menu_clientes()
        elif opcion == '3':
            menu_autos()
        elif opcion == '4':
            print("\n\t.. ¡Gracias Bye! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_revisiones():
    while True:
        borrarPantalla()
        print("""
                      .::  Menu Revisiones ::. 
                  1.- Insertar
                  2.- Consultar
                  3.- Actualizar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Insertar Revision ::. ")
            no_revision = input("\t NoRevision: ")
            cambiofiltro = input("\tCambio Filtro: ")
            cambioaceite = input("\tCambio Aceite: ")
            cambiofrenos = input("\tCambio Frenos: ")
            otros = input("\tOtros: ")
            matricula = input("\tMatricula: ")

            obj_revision = Revisiones.Revision(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
            resultado = obj_revision.insertar()
            if resultado:
                print(f"\n \t \t .:: La revision {no_revision} se creó correctamente ::. ")
            else:
                print(f"\n \t \t  ** No fue posible crear la revision {no_revision}, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n\t\t Aquí están las revisiones: \n ")
            registros = Revisiones.Revision.consultar()
            if registros:
                for fila in registros:
                    print(f"\n No. de Revisión: {fila[0]} \n Cambio de Filtro: {fila[1]} \n Cambio de Aceite: {fila[2]} \n Cambio de Frenos: {fila[3]} \n Otros: {fila[4]} \n Matrícula: {fila[5]} \n")
            else:
                print(f"\n\t ** No se encontraron registros de revisiones ** ...")
            esperarTecla()
        elif opcion == '3':
            borrarPantalla()
            no_revision = input("\t NoRevision de la revision a actualizar: ")
            cambiofiltro = input("\t Nuevo Cambio de Filtro: ")
            cambioaceite = input("\t Nuevo Cambio de Aceite: ")
            cambiofrenos = input("\t Nuevo Cambio de Frenos: ")
            otros = input("\t Nuevos Otros Cambios: ")
            matricula = input("\t Nueva Matricula: ")
            resultado = Revisiones.Revision.actualizar(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
            if resultado:
                print(f"\n \t \t .:: La Revision se actualizó con éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible actualizar la Revision, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '4':
            borrarPantalla()
            no_revision = input("\t NoRevision de la revision a eliminar: ")
            resultado = Revisiones.Revision.eliminar(no_revision)
            if resultado:
                print(f"\n \t \t .:: La Revision se eliminó con éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible eliminar la Revision, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_clientes():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Clientes ::. 
                  1.- Insertar
                  2.- Consultar
                  3.- Actualizar
                  4.- Eliminar
                  5.- Salir 
          """)
        opcion = input("\t Elige una opción: ")
        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Insertar Cliente ::. ")
            nif = input("\t Nif: ")
            nombre = input("\tNombre: ")
            direccion = input("\tdireccion: ")
            ciudad = input("\tCiudad: ")
            tel = input("\ttel: ")
            obj_clientes = Clientes.Clientes( nif, nombre, direccion, ciudad, tel)
            resultado = obj_clientes.insertar()
            if resultado:
                print(f"\n \t \t .:: El cliente {nif} se creó correctamente ::. ")
            else:
                print(f"\n \t \t  ** No fue posible crear el cliente {nif}, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n\t\t Aquí están los clientes: \n ")
            registros = Clientes.Clientes.consultar()
            if registros:
                for fila in registros:
                    print(f"\n Nif: {fila[0]} \n Nombre: {fila[1]} \n Dirección: {fila[2]} \n Ciudad: {fila[3]} \n Tel: {fila[4]} \n")
            else:
                print(f"\n\t ** No se encontraron registros de clientes ** ...")
            esperarTecla()
        elif opcion == '3':
            borrarPantalla()
            nif = input("\t Nif a actualizar: ")
            nombre = input("\t Nuevo Cambio de nombre ")
            direccion = input("\t Nuevo Cambio de direccion: ")
            ciudad = input("\t Nuevo Cambio de ciudad: ")
            tel = input("\t Nuevo cambio de telefono: ")
           
            resultado = Clientes.Clientes.actualizar(nif, nombre, direccion, ciudad, tel)
            if resultado:
                print(f"\n \t \t .:: el cliente se actualizó con éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible actualizar el cliente, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '4':
            borrarPantalla()
            nif= input("\t NoRevision de la revision a eliminar: ")
            resultado = Clientes.Clientes.eliminar(nif)
            if resultado:
                print(f"\n \t \t .:: El cliente se eliminó con éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible eliminar El cliente, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

       
def menu_autos():
    while True:
        borrarPantalla()
        print("""
                      .::  Menu Autos ::. 
                  1.- Insertar
                  2.- Consultar
                  3.- Actualizar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Insertar Auto ::. ")
            matricula = input("\t Matricula: ")
            marca = input("\t Marca: ")
            modelo = input("\t Modelo: ")
            color = input("\t Color: ")
            nif = input("\t NIF del Propietario: ")

            obj_auto = Autos.Auto(matricula, marca, modelo, color, nif)
            resultado = obj_auto.insertar()
            if resultado:
                print(f"\n \t \t .:: El auto {matricula} se creó correctamente ::. ")
            else:
                print(f"\n \t \t  ** No fue posible crear el auto {matricula}, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n\t\t Aquí están los autos: \n ")
            registros = Autos.Auto.consultar()
            if registros:
                for fila in registros:
                    print(f"\n Matricula: {fila[0]} \n Marca: {fila[1]} \n Modelo: {fila[2]} \n Color: {fila[3]} \n NIF: {fila[4]} \n")
            else:
                print(f"\n\t ** No se encontraron registros de autos ** ...")
            esperarTecla()
        elif opcion == '3':
            borrarPantalla()
            matricula = input("\t Matricula del auto a actualizar: ")
            marca = input("\t Nueva Marca: ")
            modelo = input("\t Nuevo Modelo: ")
            color = input("\t Nuevo Color: ")
            nif = input("\t Nuevo NIF del Propietario: ")
            resultado = Autos.Auto.actualizar(matricula, marca, modelo, color, nif)
            if resultado:
                print(f"\n \t \t .:: El Auto se actualizó con éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible actualizar el Auto, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '4':
            borrarPantalla()
            matricula = input("\t Matricula del auto a eliminar: ")
            resultado = Autos.Auto.eliminar(matricula)
            if resultado:
                print(f"\n \t \t .:: El Auto se eliminó con éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible eliminar el Auto, por favor verifique ** ... ")
            esperarTecla()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()
