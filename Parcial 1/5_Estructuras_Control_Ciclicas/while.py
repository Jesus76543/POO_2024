#El ciclo while es una estructura de control que itetra o repite la ejecucion de una serie de instrucciones tantas veces como la condicion se cumpla 'true'

#sintaxis:

#while condicion
   #bloque de intrucciones

#ejemplo1 crear un programa que imprima 5 veces el caracter @

contador=1
while contador<=5:
    print("@")
    contador+=1

        #ejemplo2 crear un programa que imprima los numeros dl 1 al 5#los sume y al final imprima la suma
contador=1
suma=0
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"La suma es: {suma}")

#Ejemplo3 crear un programa que solicite un numero entero y a continuaxcion imprima la tabla de multiplicar correspondiente
numero=int(input("Ingrese  un numero: "))

multi=0
i=1
while i<=10:
     multi=i*numero
     print(f"{numero} x {i} = {multi}")
     i+=1