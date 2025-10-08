import re

document = input("Digite a descrição da receita: ")

number = re.search(r"\d+", document)

print(f"O número da receita é: {number.group()}")