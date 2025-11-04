from calculate_tip import calculate_tip
from calculate_total import calculate_total

try:
    value = float(input("Digite o valor da conta: "))
    tip = float(input("Digite a porcentagem de gorjeta: "))

    tip_value = calculate_tip(tip, value)
    total = calculate_total(value, tip_value)

    print(f"Valor da gorjeta: {tip_value}")
    print(f"Total a pagar: {total}")

except ValueError:
    print("Erro, digite apenas números!")
