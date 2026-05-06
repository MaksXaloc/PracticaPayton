suma_acumulada = 0
repeticiones = 0
conitinuar = "s"
while conitinuar.lower() == "s":
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    suma_actual = num1 + num2
    print(f"El resultado de la suma es: {suma_actual}")
    suma_acumulada += suma_actual
    repeticiones += 1
    conitinuar = input("¿Deseas repetir la operacion? (s/n): ")
print(f'Mensaje: "Resumen:"')
print(f"la suma total es: {suma_acumulada} y el numero de repeticiones es: {repeticiones}")
