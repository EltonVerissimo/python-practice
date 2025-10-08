def salute(hour = ""):

    greeting = ""
    if hour <= 12:
        greeting = "Bom dia!"
    elif hour > 12 and hour <= 18:
        greeting = "Boa tarde!"
    else:
        greeting = "Boa noite!"

    return greeting

hour = int(input("Digite a hora atual (0-23): "))

print(salute(hour))