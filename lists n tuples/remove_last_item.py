itens_list = input("Pedidos feitos (separados por vírgula): ")

itens_list = itens_list.split(",")[:-1]

print("Pedidos finais: " + str(itens_list))