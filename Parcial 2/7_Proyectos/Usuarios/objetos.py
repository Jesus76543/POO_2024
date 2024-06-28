from clases import *

cliente1 = Cliente("Ana Torres Guzman", "Col Centro 1500 nte", "618123456", 1234)
empleado1 = Empleado("Daniel Fuentes Loera", "Fracc Alamedas 1300 nte", "6183335678", 1200.90, 123, "A")

print("Información del Cliente 1:")
print(cliente1.info_usuario())
    
print("\nInformación del Empleado 1:")
print(empleado1.info_usuario())

