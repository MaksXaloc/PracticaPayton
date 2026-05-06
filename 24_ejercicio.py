total_acumulado = 0
contador_operaciones = 0
while total_acumulado <= 50:
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    suma_actual = num1 + num2
    total_acumulado += suma_actual
    contador_operaciones += 1
    if contador_operaciones == 1:
        texto_operaciones = "operacion realizada"
    else:
        texto_operaciones = "operaciones realizadas"
    print(f"El resultado de la suma es: {suma_actual}")
    print(f"Total acumulado es: {total_acumulado} y llevas {contador_operaciones} {texto_operaciones}")
print(f'Mensaje: "Fin del programa"')
