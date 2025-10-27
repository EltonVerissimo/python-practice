def add_numbers(n):
    if n == 0:
        return 0
    return n + add_numbers(n-1)


number = int(input("Digite um número: "))

print(f"A soma de 1 a {number} é: " + str(add_numbers(number)))
