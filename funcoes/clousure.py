def calculate_discount(sell_value):
    def discount(discount):
        return sell_value - (sell_value * (discount/100))
    return discount

discount = float(input("Digite a porcentagem de desconto: "))
sell_value = float(input("Digite o valor da compra: "))

calculate_discount_function = calculate_discount(sell_value)
result = calculate_discount_function(discount)

print("Preço final com desconto: " + str(result))