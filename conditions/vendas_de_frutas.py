applesQuantity = int(input("Digite a quantidade de maçãs vendidas: "))
bananasQuantity = int(input("Digite a quantidade de bananas vendidas: "))

if applesQuantity == bananasQuantity:
    print("Houve um empate!")

elif applesQuantity > bananasQuantity:
    print("As maçãs tiveram mais vendas")

else:
    print("As bananas tiveram mais vendas")