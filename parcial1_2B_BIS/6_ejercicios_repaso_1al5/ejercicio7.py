inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

# Imprimir números impares entre inicio y fin
for i in range(inicio, fin + 1):
    if i % 2 != 0:
        print(i, end=" ")
