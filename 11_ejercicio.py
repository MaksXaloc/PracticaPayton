letra = input("Introduce una letra: ")
if letra.isalpha():
    es_mayuscula = letra.isupper()
    if es_mayuscula == True:
        print(f"La letra {letra} es mayúscula")
    if es_mayuscula == False:
        print(f"La letra {letra} es minuscula")
elif letra.isdigit():
    print(f"El valor introducido {letra} es un número")
else:
    print("La letra es mayúscula ¿?")
