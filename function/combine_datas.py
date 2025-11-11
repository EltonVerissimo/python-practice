def join_information(product, price):
    return f"{product}: {price}"

products = input("Digite os produtos separados por vírgula: ").split(" ")
prices = input("Digite os preços separados por vírgula: ").split(",")

for i in range(len(products)):
    print(join_information(products[i], prices[i].strip()))