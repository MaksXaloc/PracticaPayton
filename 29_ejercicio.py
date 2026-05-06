listas1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
num_valores = len(listas1)
cant_numeros = 0
cant_letras = 0
cant_mayusculas = 0
suma_numeros = 0
for elemento in listas1:
    caracter = str(elemento)
    if caracter.isdigit():
        cant_numeros += 1
        suma_numeros += int(caracter)
    elif caracter.isalpha():
        cant_letras += 1
        if caracter.isupper():
            cant_mayusculas += 1
print(f"Numero de valores: {num_valores}")
print(f"Cantidad de numeros: {cant_numeros}")
print(f"Cantidad de letras: {cant_letras}")
print(f"Cantidad de mayusculas: {cant_mayusculas}")
print(f"Suma total de numeros: {suma_numeros}")
