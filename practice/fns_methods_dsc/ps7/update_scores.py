def print_students_and_scores(students, scores):
    student_scores = {}
    for index in range(len(students)):
        student_scores[students[index]] = scores[index]

    student_scores_list = [(-v, k) for (k, v) in student_scores.items()]
    student_scores_list.sort()

    for student_score in student_scores_list:
        print(student_score[1], -student_score[0], sep=",")


students = input()
scores = input()
updates = input()

students = students.split(",")
scores = [float(score) for score in scores.split(",")]
updates = updates.split(",")

finaldict={}

for i,j in zip(students,scores):
    finaldict[i]=j

for i in updates:
    finaldict[i]+=5

students=[i for i,j in finaldict.items()]
scores=[j for i,j in finaldict.items()]

print_students_and_scores(students,scores)