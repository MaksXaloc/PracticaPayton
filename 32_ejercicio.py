import random
lista_palabras = ["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
palabra_secreta = random.choice(lista_palabras)
letras = list(palabra_secreta)
random.shuffle(letras)
intentos = 3
acertado = False
print(f"Letras desordenadas: {letras}")
while intentos > 0 and not acertado:
    respuesta = input("Introduce la palabra correcta: ")
    if respuesta.lower() == palabra_secreta:
         print("Acertaste")
         acertado = True
    else:
        intentos -= 1
        print("No has acertado")
if not acertado:
    print("No has acertado ninguno de los intentos")
