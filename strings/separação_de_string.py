import re

texto = input("Digite o nome completo e o ano de nascimento do paciente: ")

regexString = r"[A-Z][a-z]*|\d{4}"

partes_da_string = re.findall(regexString, texto)

print("Primeiro Nome: " + partes_da_string[0])
print("Sobrenome: " + partes_da_string[1])
print("Ano de Nascimento: " + partes_da_string[2])