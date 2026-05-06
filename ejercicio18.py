palabra = input("Introduce una palabra: ")
vocales_encontradas = ""
conosonantes_encontradas = ""
hay_mayuscula = False
vocales = "aeiouáéíóú"
for letra in palabra:
    if letra.isalpha():
        if letra.isupper():
         hay_mayuscula = True
        if letra in vocales:
         vocales_encontradas += letra
        else:
         conosonantes_encontradas += letra
print(f"las vocales de la palabra {palabra} son: {vocales_encontradas}")
if hay_mayuscula:
       print(f"las consonantes de la palabra {palabra} son: {conosonantes_encontradas}¿?")
else:
     print(f"las consonantes de la palabra {palabra} son: {conosonantes_encontradas}")
