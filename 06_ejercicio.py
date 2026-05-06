peso = float(input("introcuce tu peso en kg: "))
estatura = float(input("introcuce tu estatura en metros: "))
imc = peso / (estatura ** 2)
print(f"si pesas {peso} kilos y mides {estatura}, tu IMC es: {round(imc, 2)}")
print("tu IMC es:", round(imc, 2))
if imc >= 25:
    print("Hay sobrepeso")
