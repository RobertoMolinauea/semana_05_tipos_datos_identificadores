# Programa: Calculadora de compra
# Descripción: Calcula el total a pagar de un producto aplicando descuento e IVA.

def calcular_subtotal(precio_unitario, cantidad):
    return precio_unitario * cantidad


def aplicar_descuento(subtotal, tiene_descuento, porcentaje_descuento):
    if tiene_descuento:
        return subtotal - (subtotal * porcentaje_descuento / 100)
    return subtotal


def calcular_total(subtotal_con_descuento, iva):
    return subtotal_con_descuento + (subtotal_con_descuento * iva / 100)


nombre_producto = "Cuaderno"
precio_unitario = 2.50
cantidad = 4
tiene_descuento = True
porcentaje_descuento = 10
iva = 12

subtotal = calcular_subtotal(precio_unitario, cantidad)
subtotal_con_descuento = aplicar_descuento(subtotal, tiene_descuento, porcentaje_descuento)
total_pagar = calcular_total(subtotal_con_descuento, iva)

print("Producto:", nombre_producto)
print("Subtotal:", subtotal)
print("Total a pagar:", total_pagar)
