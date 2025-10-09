def calculate_age(birth_year = 0, current_year = 0):
    age = current_year - birth_year
    return age

birth_year = int(input("Digite o seu ano de nascimento: "))
current_year = int(input("Digite o ano atual: "))

print(f"A idade é {calculate_age(birth_year, current_year)} anos")