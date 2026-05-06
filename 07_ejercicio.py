num1 = int(input("introcuce el primer número:"))
num2 = int(input("introcuce el segundo número: "))
if num1 > num2:
    print(f"el número {num1} es mayor que: {num2}")
elif num2 > num1:
    print(f"el número {num2} es menor que: {num1}")
else:
    print(f"Ambos números son iguales")
