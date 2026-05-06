cantidad = int(input("Cuantos numeros vas a introducir?"))
lista_numeros = []
for i in range(cantidad):
    numero = int(input("Introduce un numero : "))
    lista_numeros.append(numero)
lista_numeros.sort()
print(lista_numeros)