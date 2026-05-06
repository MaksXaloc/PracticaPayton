import random
numero_secreto = random.randint(1, 1000)
numero_usuario = 0
intentos = 0
print("Bienvenido! He pensado un numero entre 1 y 1000. Intenta adivinarlo!")
while numero_usuario != numero_secreto:
    numero_usuario = int(input("Introduce un valor comprendido entre 1 y 1000: "))
    intentos += 1
    if numero_usuario < numero_secreto:
        print("El número que has introducido es menor")
    elif numero_usuario > numero_secreto:
        print("El número que has introducido es mayor")
print(f"Acertaste, has realizado {intentos} intentos")
