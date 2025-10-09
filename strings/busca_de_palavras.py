import re

nomes_de_livros = input("Digite o título dos livro: ")
letra_para_pesquisa = input("Digite a letra inicial para pesquisa: ")

regexString = rf"[{letra_para_pesquisa}][a-z]*"

print(re.findall(regexString, nomes_de_livros))