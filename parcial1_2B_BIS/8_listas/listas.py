#List (Array) 
#Son colleciones o conjunto de datos/valores bajo
#Un mismo nombre, para acceder a los  valores se hace con un indice numerico
#Nota sus valores si son modificables
#La lista es una coleccion ordenada y modificable Permite miembros duplicados


#Ejemplo 1 crear una liste con datos nuericos eh inmprimir el contenido
'''import os

os.system("cls")

lista=[23,34]
print(lista)

#recorrer la lista con el for

for i in lista:
    print(i)

#Recorrer la lista con el while
i=0
while i<=len(lista)-1:
    print(lista[i])
    i+=1

#Ejemplo 2 crea una lista de 4 palabras, solicitar una palabra y buscar la 
#coincidencia en la lista e indicar si la encontro o no y en que posicion 

palabras=["Hola","2024","bye","UTD"]
print(palabras)

palabra_buscar=input("Ingresa la palabra buscar: ")

noencontre=True
for i in palabras:
  if palabra_buscar==i:
     print(f"Encontre la palabara {i}, en la posicion {palabras.index (i)}")
  
     noencontre=False
if noencontre:
    print(f"No encontre la palabra")


#Ejemplo 3 while
palabras = ["Hola", "2024", "bye", "UTD"]
print(palabras)

palabra_buscar = input("Ingresa la palabra a buscar: ")

encontrada = False
indice = 0
while not encontrada and indice < len(palabras):
    if palabra_buscar == palabras[indice]:
        print(f"Encontré la palabra '{palabra_buscar}' en la posición {indice}.")
        encontrada = True
    indice += 1

if not encontrada:
    print(f"No encontré la palabra '{palabra_buscar}' en la lista")

#Ejemplo3 elimar elementos de una lista
os.system("clear")

numeros=[23,24,23]
print(numeros)

#agregar elemntos
numeros.append(100)
print(numeros)
numeros.insert(3,200)
print(numeros)

#elimnar un elemnto
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros)


#Ejempl0 4 Crear una lista multidimensional (matriz) para almacenar los contactos telefonicos

agenda=[
    ["Carlos", 6182334567],
    ["Karin", 6182334569],
    ["Leon",  6182334673],
    ["Mbappe", 618754231],

    ]
print(agenda)
 
 
for i in agenda:
    print(f"{agenda.index(i)+1} .-{i}")'''


#Ejemplo 5 Crear un programa que permita Gestionar (Administrar) peliculas,
#colocar un menu de opciones para agregar, remover,consultar peliculas.
#Notas
#1 Utilizar funciones y mandar llamar desde otro archivo
#2 Utilizar listas ´para almacenar los nombres de peliculas


# Archivo principal (main.py)

# Importamos el módulo donde definiremos las funciones
# Archivo principal (main.py)

import peliculas_gestion as pg

def mostrar_menu():
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

def main():
    peliculas = [] # Diccionario para almacenar información de las películas

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Ingresa el nombre de la película: ")
            genero_pelicula = input("Ingresa el género de la película: ")
            anio_lanzamiento = input("Ingresa el año de lanzamiento: ")
            pg.agregar_pelicula(peliculas, nombre_pelicula, genero_pelicula, anio_lanzamiento)
        elif opcion == "2":
            nombre_pelicula = input("Ingresa el nombre de la película a remover: ")
            pg.remover_pelicula(peliculas, nombre_pelicula)
        elif opcion == "3":
            pg.consultar_peliculas(peliculas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
