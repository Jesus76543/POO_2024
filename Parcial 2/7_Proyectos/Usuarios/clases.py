class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def info_usuario(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

class Cliente(Usuario):
    def __init__(self, nombre, direccion, telefono, num_cliente):
        super().__init__(nombre, direccion, telefono)
        self.num_cliente = num_cliente

    def info_usuario(self):
        return f"{super().info_usuario()}, Número de Cliente: {self.num_cliente}"

class Empleado(Usuario):
    def __init__(self, nombre, direccion, telefono, salario, num_empleado, tipo):
        super().__init__(nombre, direccion, telefono)
        self.salario = salario
        self.num_empleado = num_empleado
        self.tipo = tipo

    def info_usuario(self):
        return f"{super().info_usuario()}, Salario: {self.salario}, Número de Empleado: {self.num_empleado}, Tipo: {self.tipo}"
