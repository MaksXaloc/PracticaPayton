pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
suma_total = 0
numero = 0
print("Introduce numeros (teclea -99 para finalizar):")
for _ in range(100000):
    numero = int(input("Introduce un numero: "))
    if numero == -99:
        break
    suma_total += numero
    if numero % 2 == 0:
            pares += 1
    else:
            impares += 1
    if numero > 0:
            positivos += 1
    elif numero < 0:
            negativos += 1
    else:
            ceros += 1
print("\nRESUMEN")
print(f"El numero de pares: {pares}")
print(f"El numero de impares: {impares}")
print(f"El numero de numeros positivos: {positivos}")
print(f"El numero de numeros negativos: {negativos}")
print(f"El total es {suma_total}")
