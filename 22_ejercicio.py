continuar = "s"
while continuar.lower() == "s":
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    print(f"El resultado de la suma es: {num1 + num2}")
    continuar = input("¿Desea repetir la operación? (s/n): ")
print('Mensaje: "Programa finalizado"')
