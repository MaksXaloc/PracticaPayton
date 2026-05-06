listas_letras = []
continuar = "s"
while continuar.lower() != "n":
    letra = input("Introduce una letra: ")
    if not letra.isalpha():
        continue
    if letra not in listas_letras:
        listas_letras.append(letra)
    continuar = input("¿Deseas repetir s/n: ")
print(listas_letras)
