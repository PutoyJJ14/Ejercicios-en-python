# Factura.py

def factura():
    print("=== Emisión de Factura ===")
    
    # Solicitar datos de entrada
    articulo = input("Ingrese el nombre del artículo: ")
    precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
    cantidad = int(input("Ingrese la cantidad adquirida: "))
    
    # Calcular Sub Total
    sub_total = precio_unitario * cantidad
    
    # Aplicar descuento si corresponde
    descuento = 0
    if sub_total > 1000:
        descuento = sub_total * 0.12
    
    # Calcular IVA
    iva = (sub_total - descuento) * 0.15
    
    # Calcular Total
    total = sub_total - descuento + iva
    
    # Mostrar factura
    print("\n=== FACTURA ===")
    print(f"Artículo: {articulo}")
    print(f"Precio Unitario: ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Sub Total: ${sub_total:.2f}")
    print(f"Descuento (12% si aplica): -${descuento:.2f}")
    print(f"IVA (15%): +${iva:.2f}")
    print(f"Total a Pagar: ${total:.2f}")

# Llamar a la función principal
if __name__ == "__main__":
    factura()