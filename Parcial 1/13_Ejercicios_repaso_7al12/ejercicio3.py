#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#el contenido de la lista en mayusculas
mi_lista = []

# Pedir al usuario que ingrese palabras o frases hasta que decida detenerse
while True:
    entrada = input("Ingresa una palabra o frase (o escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
        break
    mi_lista.append(entrada)

# Imprimir el contenido de la lista en mayúsculas
for elemento in mi_lista:
    print(elemento.upper())
