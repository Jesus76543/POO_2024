from clases import *
rectangulo1 = Rectangulo(x=3, y=4, altura=10, ancho=20)
circulo1 = Circulo(x=3, y=3, radio=6)

print(f"Posición del rectángulo: ({rectangulo1.x}, {rectangulo1.y})")
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")

print(f"Posición del círculo: ({circulo1.x}, {circulo1.y})")
print(f"Área del círculo: {circulo1.calcular_area()}")

