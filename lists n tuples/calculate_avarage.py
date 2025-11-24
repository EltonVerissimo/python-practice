students_tips = input("Digite as notas dos alunos separadas por vírgula: ")

students_tips_list = students_tips.split(",")
students_tips_to_int = [int(item) for item in students_tips_list]

avarage = sum(students_tips_to_int) / len(students_tips_to_int)

print("Média final da turma: " + str(avarage))