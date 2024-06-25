 #Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
 #a.- Recorrer la lista y mostrarla
 #b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 #c.- ordenarla y mostrarla
 #d.- mostrar su longitud
 #e.- buscar algun elemento que el usuario pida por teclado

def mostrar_lista(lista):
    for numero in lista:
        print(numero, end=" ")

def lista_a_string(lista):
    return " ".join(str(numero) for numero in lista)
numeros = [5, 12, 8, 3, 20, 15, 7, 10]
print("a. Lista original:")
mostrar_lista(numeros)
print("\n")

lista_como_string = lista_a_string(numeros)
print(f"b. Lista como string: {lista_como_string}\n")

numeros.sort()
print("c. Lista ordenada:")
mostrar_lista(numeros)
print("\n")

print(f"d. Longitud de la lista: {len(numeros)}\n")

elemento_buscar = int(input("e. Ingresa un número para buscar en la lista: "))
if elemento_buscar in numeros:
    print(f"El número {elemento_buscar} está en la lista.")
else:
    print(f"El número {elemento_buscar} no está en la lista.")
