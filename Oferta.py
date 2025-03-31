# Programa para calcular el monto de la compra, descuento, monto a pagar y unidades de obsequio

def calcular_oferta(cantidad_docenas, precio_por_docena):
    # Calcular el monto de la compra
    monto_compra = cantidad_docenas * precio_por_docena

    # Determinar el descuento y las unidades de obsequio
    if cantidad_docenas > 3:
        descuento = monto_compra * 0.15
        unidades_obsequio = (cantidad_docenas - 3) * 1  # Una unidad por cada docena en exceso
    else:
        descuento = monto_compra * 0.10
        unidades_obsequio = 0

    # Calcular el monto a pagar
    monto_a_pagar = monto_compra - descuento

    return monto_compra, descuento, monto_a_pagar, unidades_obsequio


# Entrada de datos
cantidad_docenas = int(input("Ingrese la cantidad de docenas compradas: "))
precio_por_docena = float(input("Ingrese el precio por docena: "))

# Cálculo
monto_compra, descuento, monto_a_pagar, unidades_obsequio = calcular_oferta(cantidad_docenas, precio_por_docena)

# Salida de resultados
print("\nResultados:")
print(f"Monto de la compra: ${monto_compra:.2f}")
print(f"Monto del descuento: ${descuento:.2f}")
print(f"Monto a pagar: ${monto_a_pagar:.2f}")
print(f"Unidades de obsequio: {unidades_obsequio}")