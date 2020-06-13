from collections import OrderedDict
n=int(input())
matches=[]
for i in range(n):
    matches.append(input().split(';'))
teams=[]
for i in matches:
    teams.append(i[0])
    teams.append(i[1])
teams=list(set(teams))
d={}
for i in teams:
    d[i]={'MP':0,'W':0,'D':0,'L':0,'P':0}

for i in matches:
    if i[2]=='win':
        d[i[0]]['MP']+=1
        d[i[1]]['MP']+=1
        d[i[0]]['W']+=1
        d[i[0]]['P']+=3
        d[i[1]]['L']+=1
    elif i[2]=='loss':
        d[i[0]]['MP']+=1
        d[i[1]]['MP']+=1
        d[i[0]]['L']+=1
        d[i[1]]['W']+=1
        d[i[1]]['P']+=3
    else:
        d[i[0]]['MP']+=1
        d[i[1]]['MP']+=1
        d[i[0]]['D']+=1
        d[i[0]]['P']+=1
        d[i[1]]['D']+=1
        d[i[1]]['P']+=1
        
d=OrderedDict(sorted(d.items(),key = lambda x: (-1*(x[1]['P']),x[0])))

print('{:<23} | MP |  W |  D |  L |  P |'.format('Team'))
for i in d.items():
    print('{:<23} | {:2} | {:2} | {:2} | {:2} | {:2} |'.format(i[0],i[1]['MP'],i[1]['W'],i[1]['D'],i[1]['L'],i[1]['P']))
