suma_total = 0

while True:
    numero = int(input("Ingrese números enteros "))
    
    if numero == 0:
        break

    suma_total += numero

print(f"El resultado total es {suma_total}")