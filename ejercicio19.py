a = int(input("Introduce el primer intervalo: "))
b = int(input("Introduce el segundo intervalo: "))
resultado = ""
if a < b:
    for i in range(a, b + 1, 1):
        resultado += str(i) + "-" 
elif a > b:
    for i in range(a, b - 1, -1):
        resultado += str(i) + "-"
else:
    resultado = str(a) + "-"
print(resultado[:-1])