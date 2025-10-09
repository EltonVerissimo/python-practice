import re

name = input("Digite o nome do cliente para validação: ")

padrao_nome = r'[A-Z][a-z]*'

if re.fullmatch(padrao_nome, name):
    print("Nome válido")
else:
    print("Nome inválido")