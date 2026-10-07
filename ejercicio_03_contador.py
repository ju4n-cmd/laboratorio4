"""
EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales (a, e, i, o, u) que tiene la palabra.
"""

cantidad_vocales = 0
frase = input("Escriba su frase: ")
for letra in frase:
    if letra in "aeiouAEIOU":
        cantidad_vocales += 1

print(f"La cantidad total de vocales en su frase/texto es: {cantidad_vocales}")

