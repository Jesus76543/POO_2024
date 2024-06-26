from Clases import Rectangulo, Circulo, Triangulo

def main():
    rectangulo = Rectangulo(5.0, 3.0)
    circulo = Circulo(2.5)
    triangulo = Triangulo(4.0, 6.0)

    print(f"Área del Rectángulo: {rectangulo.CalcularArea():.2f}")
    print(f"Área del Círculo: {circulo.CalcularArea():.2f}")
    print(f"Área del Triángulo: {triangulo.CalcularArea():.2f}")

if __name__ == "__main__":
    main()
