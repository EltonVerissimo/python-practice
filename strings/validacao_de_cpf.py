import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

padrao_cpf = r'[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}'

if re.fullmatch(padrao_cpf, cpf):
    print("O CPF está no formato correto")
else:
    print("O CPF não está no formato correto")