def agregar_peliculas(diccionario_peliculas, nombre, genero, anio):
    diccionario_peliculas[nombre] = {"Género": genero, "Año de lanzamiento": anio}
    print(f"La película '{nombre}' ha sido agregada.")

def remover_pelicula(diccionario_peliculas, nombre):
    if nombre in diccionario_peliculas:
        del diccionario_peliculas[nombre]
        print(f"La película '{nombre}' ha sido removida.")
    else:
        print(f"La película '{nombre}' no está en la lista.")

def consultar_peliculas(diccionario_peliculas):
    if diccionario_peliculas:
        print("Lista de películas:")
        for nombre, info in diccionario_peliculas.items():
            print(f"- {nombre} ({info['Género']}, {info['Año de lanzamiento']})")
    else:
        print("No hay películas en la lista.")

def actualizar_pelicula(diccionario_peliculas, nombre, genero, anio):
    if nombre in diccionario_peliculas:
        diccionario_peliculas[nombre]["Género"] = genero
        diccionario_peliculas[nombre]["Año de lanzamiento"] = anio
        print(f"La película '{nombre}' ha sido actualizada.")
    else:
        print(f"La película '{nombre}' no está en la lista.")

def buscar_pelicula(diccionario_peliculas, nombre):
    if nombre in diccionario_peliculas:
        info = diccionario_peliculas[nombre]
        print(f"Detalles de la película '{nombre}':")
        print(f"- Género: {info['Género']}")
        print(f"- Año de lanzamiento: {info['Año de lanzamiento']}")
    else:
        print(f"La película '{nombre}' no está en la lista.")

def vaciar_lista(diccionario_peliculas):
    diccionario_peliculas.clear()
    print("La lista de películas ha sido vaciada.")