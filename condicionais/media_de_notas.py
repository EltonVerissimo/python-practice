grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
grade3 = float(input("Digite a terceira nota: "))

result = (grade1 + grade2 + grade3) / 3

print(f"Média: {round(result, 2)}")

if result >= 7:
    print("Aprovado(A)")
elif 5 <= result < 7:
    print("Recuperação")
else:
    print("Reprovado(A)")