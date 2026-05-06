import math
num = float(input("introcuce un numero: "))
raiz = math.sqrt(num)
raiz_redondeada = round(raiz, 1)
division = int(raiz / 2)
print("el resultado de la raiz es:", raiz_redondeada)
print("el resultado de la division es:", division)