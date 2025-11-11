current_hour = int(input("Digite a hora atual (formato 24 horas: ): "))

if 18 > current_hour > 8:
    print("Acesso permitido.")
else:
    print("Acesso negado.")