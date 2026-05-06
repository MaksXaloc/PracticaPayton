import random
lista_palabras = ["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
palabra_secreta = random.choice(lista_palabras)
intento_usuario= ""
print("He elegido una palabra al azar de la lista, intenta adivinarla.")
while intento_usuario.lower() != palabra_secreta:
    intento_usuario = input("Introduce la palabra secreta: ")
    if intento_usuario.lower() != palabra_secreta:
        print("SIGUE JUGANDO")
print("ACERTASTE")