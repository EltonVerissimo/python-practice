def sellers_calculator(sellers:str):
    sellers_list = sellers.split(" ")
    total = 0

    for x in sellers_list:
        total += int(x)
    
    return str(total)

sellers = str(input("Digite os valores das vendas: "))

print("O total de vendas foi: " + str(sellers_calculator(sellers)))