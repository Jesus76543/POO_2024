def calcular_imc():
    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))
        
        imc = peso / (altura ** 2)
        print(f"Tu IMC es: {imc:.2f}")

        if imc < 18.5:
            print("Composición corporal: Peso inferior al normal")
        elif 18.5 <= imc < 25.0:
            print("Composición corporal: Normal")
        elif 25.0 <= imc < 30.0:
            print("Composición corporal: Peso superior al normal")
        else:
            print("Composición corporal: Obesidad")

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos para peso y altura.")

def main():
    contador_calculos = 0  
    while True:
        calcular_imc()
        contador_calculos += 1  
        respuesta = input("¿Deseas realizar otro cálculo de IMC? (s/n): ")
        if respuesta.lower() != "s":
            break

    print(f"Se realizaron un total de {contador_calculos} cálculos de IMC.")

if __name__ == "__main__":
    main()
