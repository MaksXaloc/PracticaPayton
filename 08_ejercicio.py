while True:
    num1 = int(input("introcuce el primer número entre 0 y 10:"))
    if 0 <= num1 <= 10:
        break # Si el número es válido, salimos del bucle
    else:
        print("Uno o los dos números están fuera de los límites establecidos")
while True:
    num2 = int(input("introcuce el segundo número entre 0 y 10: "))
    if 0 <= num2 <= 10:
        break # Si el número es válido, salimos del bucle
    else:
        print("Uno o los dos números están fuera de los límites establecidos")
if num1 > num2:
    print(f"el número {num1} es mayor que: {num2}")
elif num2 > num1:
    print(f"el número {num2} es menor que: {num1}")
else:
    print(f"Ambos números son iguales")        
