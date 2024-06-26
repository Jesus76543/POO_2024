class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mostrar(self):
        self.visible = True
    
class Rectangulo(Figura):
    def __init__(self, x, y, altura, ancho):
        super().__init__(x, y)
        self.altura = altura
        self.ancho = ancho

    def calcular_area(self):
        return self.altura * self.ancho
    
    def getAltura(self):
      return self.altura
    
    
    def getAncho(self):
      return self.ancho
    
    def getInfo(self):
        print(f"La altura del rectangulo es: {self.getAltura()} El ancho  del rectangulo es: {self.getAncho()}")

class Circulo(Figura):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2
    
    def getRadio(self):
        return self.radio
    
    def getInfo(self):
        print(f"El Radio del circulo es: {self.getRadio()}")


