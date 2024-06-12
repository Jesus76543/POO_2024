#Escribir un programa  que añada valores a una lista mientras que su longitud 
#sea menor a 120, y luego mostrar la lista: Usar un while y for


mi_lista = []
while len(mi_lista) < 120:
    valor = int(input("Ingresa un número (o un valor negativo para salir): "))
    if valor < 0:
        break
    mi_lista.append(valor)
print("Lista final:")
print(mi_lista)
