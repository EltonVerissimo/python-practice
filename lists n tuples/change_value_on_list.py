current_list = ['Ana', 'Carlos', 'Pedro']

wrong_name = input("Digite o nome incorreto: ")
right_name = input("Digite o nome correto: ")

item_index = current_list.index(wrong_name)

current_list.remove(wrong_name)
current_list.insert(item_index, right_name)

print(f"O nome {wrong_name} foi substituído por {right_name}.")
print("Lista atualizada: " + str(current_list))