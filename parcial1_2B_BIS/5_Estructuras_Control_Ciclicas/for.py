"""este ciclo es un ciclo interativo y se ejecuta x veces de acuerdo a los valores numericos enteros establecidos"""

#sintaxis:
#for variable in elemento_iterable(lista rango,etc):
# bloque de instrucciones

#ejemplo1 crear un programa que imprima 5 veces el caracter @

for contador in range(1,6):
    print("@")

    #ejemplo2 crear un programa que imprima los numeros dl 1 al 5#los sume y al final imprima la suma
suma=0
for numero in range(1,6):
      print(numero)
      suma+=numero
print(f"La suma es: {suma}")

#Ejemplo3 crear un programa que solicite un numero entero y a continuaxcion imprima la tabla de multiplicar correspondiente
numero=int(input("Ingrese  un numero: "))

for i in range (1,11):
     multi=i*numero
     print(f"{numero} x {i} = {multi}")