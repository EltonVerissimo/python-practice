def filter_even_numbers(number):
    return int(number) % 2 == 0

numbers = input("Digite os números separados por espaço: ")

numbers_list = numbers.split(" ")

even_numbers_filter = filter(filter_even_numbers, numbers_list)
even_numbers_list = list(even_numbers_filter)

print("Números pares: " + " ".join(even_numbers_list))