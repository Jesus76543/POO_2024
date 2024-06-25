#Los errores de excepciones en un lenguaje de programacion no es otra cosa que los errores en tiempo de ejecucion 
#Cuando se manejan los errores mediante las excepciones en realidad se dice que se evita que se presenten esos errores en el programa
#En tiempo de ejecucion 
#Ejemplo Se presenta un error cuando n o es generada una variable

# Ejemplo 1: Manejo de errores al ingresar un nombre
try:
    nombre = input("Dame el nombre completo de una persona: ")
    if len(nombre) > 0:
        nombre_usuario = "El nombre del usuario en el sistema es: " + nombre
        print(nombre_usuario)
    else:
        print("Es necesario introducir un nombre de una persona, amigo.")
except:
    print("Ocurrió un error al procesar el nombre. Verifica por favor.")

# Ejemplo 2: Manejo de errores al ingresar un número
try:
    numero = int(input("Ingresa un número entero: "))
    if numero > 0:
        print("Soy un número positivo")
    else:
        print("Soy un número negativo")
except ValueError:
    print("No es posible convertir una letra a un número. Verifica por favor.")

# Ejemplo 3: Manejo de múltiples excepciones
try:
    numero = int(input("Ingresa un número: "))
    print("El cuadrado del número es: " + str(numero * numero))
except TypeError:
    print("Es necesario convertir el número a entero.")
except ValueError:
    print("No es posible convertir una letra a un número. Verifica por favor.")
else:
    print("Todo se ejecuto sin errores")
finally:
    print("Ya termino")