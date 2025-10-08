weight = float(input("Digite seu peso (kg): "))
height = float(input("Digite sua altura (m): "))

imc = weight / (height ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Seu peso está normal.")
else:
    print("Você está acima do peso.")