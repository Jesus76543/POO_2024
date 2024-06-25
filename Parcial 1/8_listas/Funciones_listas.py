paises=["Mexico","USA","Brasil","Japon"]
numeros=[23,34,12.56,0.100,23]
texto=["Hola",True,23,3.141516]

#Ordenar una lista
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#Añadir texto
print(texto)
texto.insert(len(texto),"True")
print(texto)
texto.insert(len(texto),True)#Inserta un valor en una posiciojn especifica
print(texto)
texto.append(False)#Inserta un valor al final o donde existe un espacio en la lista
print(texto)



#eliminar elementos

print(numeros)
numeros.remove(23)
print(numeros)
numeros.pop(0)
print(numeros)

#Dar la vuelta a una lista
print(numeros)
numeros.reverse #Ordenar descendente
print(numeros)

#Buscar un dato dentro de una lista
respuesta="Brasil" in paises
print(respuesta)

#Cuantas veces aparece un valor de una lista
print(numeros)
numeros.append(23)
cuantos=numeros.count(230)
print (f"El numero 23 se encontro: {cuantos}")

#Unir listas 
print(paises)
paises.extend(numeros)
print(paises)