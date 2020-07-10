#Input-
#first line contains no. of students
#after that each line for each student: name,marks in M,marks in P,marks in C

#ex:
#2
#sumanth,23,45,56
#gopi,12,78,95

n=int(input())
a=[]
for i in range(n):
    a.append(input().split(','))

for i in range(3):
    print('+',end='')
    for j in range(25):
        print('-',end='')
        if(j==24):
            print('+',end='')
    for k in range(3):
         print('----+',end='')
         if(k==2):
             print()
    if(i==0):
        print('| {:23} |  M |  P |  C |'.format("Student"))
    if(i==1):
        for l in range(n):
            print('| {name:<23} | {m:>2} | {p:>2} | {c:>2} |'.format(name=a[l][0],m=a[l][1],p=a[l][2],c=a[l][3]))
