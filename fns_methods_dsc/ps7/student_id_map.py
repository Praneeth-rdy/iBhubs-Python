def print_students_and_ids(students, ids):
    student_ids = {}
    for index in range(len(students)):
        student_ids[students[index]] = ids[index]

    student_ids_list = [[k, v] for (k, v) in student_ids.items()]
    student_ids_list=sorted(student_ids_list,key=lambda x:x[0])

    for student in student_ids_list:
        print(student[0], student[1], sep=',')


students = input()
ids = input()

students = students.split(",")
ids = ids.split(",")

print_students_and_ids(students, ids)