"""
EJERCICIO 01: Tabla de multiplicar

1. Pide al usuario ingresar un número
2. Garantice la entrada correcta
3. Imprime la tabla de multiplicar del 1 al 10 del número ingresado. Utilice un bucle for
"""
def tabla_multiplicar():
    while True:
        entrada = input("Ingresa un número entero: ")
        if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
            numero = int(entrada)
            break
        else:
            print("Por favor, ingresa un número entero válido.")

    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabla_multiplicar()
