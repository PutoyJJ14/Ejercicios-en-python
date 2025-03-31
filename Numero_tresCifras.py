# Programa para verificar si un número de tres cifras es igual al revés del número

# Leer el número de tres cifras
numero = input("Ingrese un número de tres cifras: ")

# Validar que el número tenga exactamente tres cifras
if len(numero) == 3 and numero.isdigit():
    # Verificar si el número es igual al revés
    if numero == numero[::-1]:
        print("El número es igual al revés.")
    else:
        print("El número no es igual al revés.")
else:
    print("Por favor, ingrese un número válido de tres cifras.")