letra = input("Introduce una letra: ")
if letra.isalpha():
    es_mayuscula = letra.isupper()
    if es_mayuscula == True:
        print(f"La letra {letra} es mayúscula")
    if es_mayuscula == False:
        print(f"La letra {letra} es minuscula")
else:
    print("La letra es mayúscula ¿?")
