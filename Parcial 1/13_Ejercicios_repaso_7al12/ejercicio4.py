#Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def imprimir_tipo(variable):
    """
    Imprime un mensaje según el tipo de dato de la variable.
    """
    if isinstance(variable, int):
        print(f"La variable es un entero: {variable}")
    elif isinstance(variable, str):
        print(f"La variable es una cadena: {variable}")
    elif isinstance(variable, bool):
        print(f"La variable es un valor lógico: {variable}")
    elif isinstance(variable, list):
        print(f"La variable es una lista: {variable}")
    else:
        print(f"Tipo de dato no reconocido para la variable: {variable}")

# Crear las variables
mi_lista = [7, 4, 1]
mi_cadena = "Hola"
mi_entero = 65
mi_logico = True

# Imprimir mensajes según el tipo de dato
imprimir_tipo(mi_lista)
imprimir_tipo(mi_cadena)
imprimir_tipo(mi_entero)
imprimir_tipo(mi_logico)
