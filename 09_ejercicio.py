import math
print("Cálculo de ecuación de segundo grado: ax^2 + bx + c = 0")
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
if a == 0:
    print("La ecuación no es de segundo grado.")
else:
    discriminante = (b**2) - (4*a*c)
    if discriminante < 0:
        print("La raíz no puede ser un valor negativo")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La ecuación tiene una única solución: x = {x}")
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"El valor de x1 = {x1}")
        print(f"El valor de x2 = {x2}")    
