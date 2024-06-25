class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositaste ${cantidad}. Nuevo saldo: ${self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiraste ${cantidad}. Nuevo saldo: ${self.__saldo}")
        else:
            print("Cantidad no válida o fondos insuficientes.")

    def consultar_saldo(self):
        print(f"El saldo actual es: ${self.__saldo}")

    def get_titular(self):
        return self.__titular

    def set_titular(self, nuevo_titular):
        if nuevo_titular:
            self.__titular = nuevo_titular
            print(f"El titular de la cuenta ha sido actualizado a: {nuevo_titular}")
        else:
            print("El nombre del titular no puede estar vacío.")


# Crear una instancia de CuentaBancaria
mi_cuenta = CuentaBancaria("Juan Pérez", 1000)

# Interactuar con la cuenta a través de sus métodos públicos
mi_cuenta.consultar_saldo()  # El saldo actual es: $1000
mi_cuenta.depositar(500)     # Depositaste $500. Nuevo saldo: $1500
mi_cuenta.retirar(300)       # Retiraste $300. Nuevo saldo: $1200
mi_cuenta.set_titular("Maria López")  # El titular de la cuenta ha sido actualizado a: Maria López
print(f"El titular de la cuenta es: {mi_cuenta.get_titular()}")  # El titular de la cuenta es: Maria López
