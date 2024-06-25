#Crear un programa que calcule y obtenga el total a pagar por un producto determinado.Se debera de solicitar el nombre o descripcion del producto codigo del producto cantidad del producto precio unitario.
#El total a pagar incluye el iva y el descuento.
#Si se compran de uno acinco productos se otorga el 10% de descuento si se compran de 6 a 10 el 15% de descuento y si se compran mas de 10 el 20% de descuento
def calcular_total_a_pagar():
    # Solicitar datos al usuario
    nombre_producto = input("Ingrese el nombre o descripción del producto: ")
    codigo_producto = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))

    # Calcular el subtotal (sin descuento)
    subtotal = cantidad * precio_unitario

    # Aplicar descuento según la cantidad comprada
    if 1 <= cantidad <= 5:
        descuento = subtotal * 0.10
    elif 6 <= cantidad <= 10:
        descuento = subtotal * 0.15
    else:
        descuento = subtotal * 0.20

    # Calcular el total con descuento
    total_con_descuento = subtotal - descuento

    # Calcular el IVA (16% en México)
    iva = total_con_descuento * 0.16

    # Calcular el total a pagar
    total_a_pagar = total_con_descuento + iva

    # Mostrar resultados
    print(f"Producto: {nombre_producto} (Código: {codigo_producto})")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total con descuento: ${total_con_descuento:.2f}")
    print(f"IVA (16%): ${iva:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")

# Llamar a la función principal
calcular_total_a_pagar()


