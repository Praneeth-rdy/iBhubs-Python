def print_students_and_scores(students, scores):
    student_scores = {}
    for index in range(len(students)):
        student_scores[students[index]] = scores[index]

    student_scores_list = [(-v, k) for (k, v) in student_scores.items()]
    student_scores_list.sort()

    for student_score in student_scores_list:
        print(student_score[1], -student_score[0], sep=",")


outdated = input().split(' ')
fresh = input().split(' ')

outdated=[i.split(',') for i in outdated]
fresh=[i.split(',') for i in fresh]

finaldict={}

for i in outdated:
    finaldict[i[0]]=float(i[1])

for student in fresh:
    finaldict.update({student[0]: float(student[1])})

students = [k for k,v in finaldict.items()]
scores = [v for k,v in finaldict.items()]

print_students_and_scores(students, scores)