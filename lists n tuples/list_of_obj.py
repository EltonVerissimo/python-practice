students_list = []

student_info = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ")

student_info = student_info.split(",")
counter = 0

while counter < len(student_info):
    students_list.append({
        "Aluno": student_info[counter],
        "Idade": student_info[counter+1],
        "Nota": student_info[counter+2]
    })
    counter += 3

for student in students_list:
    print("Aluno: " + student["Aluno"])
    print("Idade: " + student["Idade"])
    print("Nota: " + student["Nota"])
    print()