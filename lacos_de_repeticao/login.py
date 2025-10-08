username = ""
password = ""
validLogin = False

while not validLogin:
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    if len(username) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(password) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    validLogin = True