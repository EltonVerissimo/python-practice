renda = int(input("Digite o valor da sua renda mensal: "))
parcela = int(input("Digite o valor da parcela desejada: "))

if renda > 2000 and parcela < (renda * 0.3):
    print("Empréstimo aceito: parcela abaixo de 30% de renda")
else:
    print("Empréstimo negado: parcela acima de 30% de renda")
