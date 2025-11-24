current_list = ['Ana', 'Pedro', 'Carlos']

new_name = str(input("Digite o nome do novo convidado: "))

position = int(input("Digite a posição na qual deseja inserir o convidado: "))

current_list.insert(position, new_name)

print("Lista atualizada de convidados: " + str(current_list))