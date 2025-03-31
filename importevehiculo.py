# Definición de la función para calcular el importe según el tipo de vehículo


def calcular_importe(tipo_vehiculo, distancia, peso_camion=None):
    
    # Definir el conjunto de vehículos y sus tarifas
    tarifas = {
        "bicicleta": 100,
        "moto": 30,
        "carro": 30,
        "camion": lambda km, ton: 30 * km + 25 * ton
    }

    # Calcular el importe según el tipo de vehículo
    if tipo_vehiculo == "bicicleta":
        return tarifas["bicicleta"]
    elif tipo_vehiculo in ["moto", "carro"]:
        return tarifas[tipo_vehiculo] * distancia
    elif tipo_vehiculo == "camion" and peso_camion is not None:
        return tarifas["camion"](distancia, peso_camion)
    else:
        return "Vehículo no válido o falta información."

# Ejemplo de uso

vehiculo = input("Introduce el tipo de vehículo (bicicleta, moto, carro, camion): ").lower()
kilometros = float(input("Introduce los kilómetros recorridos: "))

if vehiculo == "camion":
    toneladas = float(input("Introduce el peso en toneladas del camión: "))
    importe = calcular_importe(vehiculo, kilometros, toneladas)
else:
    importe = calcular_importe(vehiculo, kilometros)

print(f"El importe a pagar es: {importe} córdobas.")
