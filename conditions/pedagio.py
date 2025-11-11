distance = int(input("Digite a distância percorrida (em km): "))
result = 0

if distance > 100:
    result = 30

elif 200 >= result > 100:
    result = 20

else:
    result = 10

print(f"Valor do pedágio: R$ {result},00")