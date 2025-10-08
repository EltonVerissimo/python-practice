import re

text = input("Digite o texto a ser revisado: ")
tokenToReplace = input("Qual palavra deseja substituir?")
newToken = input("Qual a nova palavra?")

if tokenToReplace in text:
    print(re.sub(tokenToReplace, newToken, text))
else:
    print("Palavra não encontrada!")
