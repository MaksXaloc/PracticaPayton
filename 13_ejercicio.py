frase = input("Introduce una frase: ")
longitud = len(frase)
if longitud == 11:
    print("La frase tiene 11 caracteres")
elif longitud < 11:
    print("La frase tiene menos de 11 caracteres")
elif longitud > 11:
    print("La frase tiene 11 o más caracteres")
