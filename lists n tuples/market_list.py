itens_list = ["Farinha", "Sal", "Legumes"]

item = str(input("Digite o item que você quer verificar: "))

if item.capitalize() in itens_list:
    print(f"{item} está disponível!")
else:
    print(f"O item {item} precisa ser comprado!")