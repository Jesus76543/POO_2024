import peliculas_gestion as pg
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Actualizar película")
    print("5. Buscar película")
    print("6. Vaciar lista")
    print("7. Salir")

def main():
    peliculas = {}  # Diccionario para almacenar información de las películas

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Ingresa el nombre de la película: ")
            genero_pelicula = input("Ingresa el género de la película: ")
            anio_lanzamiento = input("Ingresa el año de lanzamiento: ")
            agregar_pelicula(peliculas, nombre_pelicula, genero_pelicula, anio_lanzamiento)
        elif opcion == "2":
            nombre_pelicula = input("Ingresa el nombre de la película a remover: ")
            remover_pelicula(peliculas, nombre_pelicula)
        elif opcion == "3":
            consultar_peliculas(peliculas)
        elif opcion == "4":
            nombre_pelicula = input("Ingresa el nombre de la película a actualizar: ")
            genero_pelicula = input("Ingresa el nuevo género de la película: ")
            anio_lanzamiento = input("Ingresa el nuevo año de lanzamiento: ")
            actualizar_pelicula(peliculas, nombre_pelicula, genero_pelicula, anio_lanzamiento)
        elif opcion == "5":
            nombre_pelicula = input("Ingresa el nombre de la película a buscar: ")
            buscar_pelicula(peliculas, nombre_pelicula)
        elif opcion == "6":
            vaciar_lista(peliculas)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()