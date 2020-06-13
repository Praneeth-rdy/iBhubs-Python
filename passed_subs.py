#Input:
#The first line contains Ai, names of students with maths score separated by',' 
#The second line contains Mi, maths scores separated by ','
#The third line contains Bi, names of students with physics score separated by"
#The fourth line contains Pi, physics scores separated by ','
#The fifth line contains Ci, names of students with chemistry score separated by '
#The sixth line contains Hi, chemistry scores separated by','
#The seventh line contains Ti, threshold(filter) scores for maths. physics, and chemistry separated by ','

#output:
#The first line of output contains the names of students who meet either of the minimum score criteria in the lexicographical order.
#The second line of output contains student names who passed all thei criteria mentioned above in the lexicographical order.
#If there are no students that match either of the above criteria print "No Students" for that particular line and print names(if any) for the other filter.

maths=dict(zip(input().split(','),[float(i) for i in input().split(',')]))

physics=dict(zip(input().split(','),[float(i) for i in input().split(',')]))

chem=dict(zip(input().split(','),[float(i) for i in input().split(',')]))

m,p,c=tuple([float(i) for i in input().split(',')])

pass_maths=[x for x in maths if maths[x]>=m]
pass_physics=[x for x in physics if physics[x]>=p]
pass_chem=[x for x in chem if chem[x]>=c]

pass_either= set(pass_maths)|set(pass_physics)|set(pass_chem)
pass_all=set(pass_maths)&set(pass_physics)&set(pass_chem)

pass_either=list(pass_either)
pass_either.sort()
pass_either=','.join(pass_either)
pass_all=list(pass_all)
pass_all.sort()
pass_all=','.join(pass_all)

if len(pass_either)==0:
    print('No Students')
else:
    print(pass_either)
    
if len(pass_all)==0:
    print('No Students')
else:
    print(pass_all)
