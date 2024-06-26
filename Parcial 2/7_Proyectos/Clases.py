

class Figura:
    def CalcularArea(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo

    def CalcularArea(self):
        return self.ancho * self.largo

# Otras clases (Círculo, Triángulo) también aquí...
