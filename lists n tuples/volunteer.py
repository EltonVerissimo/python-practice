volunteers = []
input_data = ""

while True:
    input_data = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    if input_data == "sair":
        break
    volunteers.append(input_data)

print("Voluntários registrados: " + str(volunteers))