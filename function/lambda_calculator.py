add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
operation = input("Escolha a operação (| + | - | * | / |): ")
result = 0

if operation == '+':
    result = add(number1, number2)
elif operation == '-':
    result = sub(number1, number2)
elif operation == '*':
    result = mul(number1, number2)
elif operation == '/':
    result = div(number1, number2)
else:
    print("Operação inválida!")

print("O resultado é: " + str(result))