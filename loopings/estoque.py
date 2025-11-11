count = 10

while count > 0:
    count -= 1
    print("Venda realizada! Estoque restante: " + str(count))

    if count == 0:
        print("Estoque esgotado")
