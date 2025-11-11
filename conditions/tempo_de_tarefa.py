taskA = 0
taskB = 0
taskC = 0
result = 0

taskA = int(input("Informe os dias para a atividade A: "))
taskB = int(input("Informe os dias para a atividade B: "))
taskC = int(input("Informe os dias para a atividade C: "))

if taskA < 0 or taskB < 0 or taskC < 0:
    print("Erro: Os dias não podem ser negativos.")
else:
    result = taskA + taskB + taskC
    print(f"Total de dias para as 3 tarefas: {result}")