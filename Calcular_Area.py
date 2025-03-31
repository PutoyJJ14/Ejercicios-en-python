import math

def calcular_area():
    while True:
        print("\nMenú de cálculo de áreas:")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Círculo")
        print("4. Triángulo")
        print("5. Trapecio")
        print("6. Salir")

        opcion = int(input("Seleccione una opción (1-6): "))

        if opcion == 1:
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = lado ** 2
            print(f"El área del cuadrado es: {area:.2f}")
        elif opcion == 2:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = base * altura
            print(f"El área del rectángulo es: {area:.2f}")
        elif opcion == 3:
            radio = float(input("Ingrese el radio del círculo: "))
            area = math.pi * radio ** 2
            print(f"El área del círculo es: {area:.2f}")
        elif opcion == 4:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
            print(f"El área del triángulo es: {area:.2f}")
        elif opcion == 5:
            base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            base_menor = float(input("Ingrese la base menor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            area = ((base_mayor + base_menor) * altura) / 2
            print(f"El área del trapecio es: {area:.2f}")
        elif opcion == 6:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 6.")

        repetir = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if repetir != 's':
            print("Saliendo del programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    calcular_area()