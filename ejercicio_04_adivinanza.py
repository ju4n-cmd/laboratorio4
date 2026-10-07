"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""

numero_secreto = 12

while True:
    intento = int(input("Intente acertar colocando un número: "))

    if intento < numero_secreto:
        print(f"El número que ha ingresado es menor que el número secreto")

    if intento > numero_secreto:
        print(f"El número que ha ingresado es mayor que el número secreto")

    if intento == numero_secreto:
        print(f"Felicidades, usted ha adivinado el número secreto!")
        break