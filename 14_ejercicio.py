total_pares = 0
total_impares = 0
for i in range(1, 51):
    if i % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1
print(f"Total de pares es: {total_pares}")
print(f"Total de impares es: {total_impares}")
