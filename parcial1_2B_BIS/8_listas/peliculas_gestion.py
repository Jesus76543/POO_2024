# Archivo peliculas_gestion.py

# Archivo peliculas_gestion.py

def agregar_pelicula(diccionario_peliculas, nombre, genero, anio):
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
