from validate_cpf import validate_cpf

try:
    cpf_number = int(input("Digite o seu CPF: "))
    isValidCPF = validate_cpf(cpf_number)

    print("CPF válido.") if isValidCPF else print("Erro: O CPF deve ter exatamente 11 dígitos.")

except ValueError:
    print("Erro: O CPF deve conter apenas números.")