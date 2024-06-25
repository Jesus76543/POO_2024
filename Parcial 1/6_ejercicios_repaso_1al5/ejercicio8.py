def calcular_porcentaje(numero, porcentaje):
    return (numero * porcentaje) / 100

valor_original = int(input("Ingrese un numero: "))
porcentaje_deseado = int(input("Ingrese el porcentaje deseado: "))
resultado = calcular_porcentaje(valor_original, porcentaje_deseado)

print(f"{porcentaje_deseado}% de {valor_original} es igual a {resultado}")
