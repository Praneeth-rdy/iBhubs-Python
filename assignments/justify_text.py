
n=int(input())
text=input().split(' ')

lengths=[len(i) for i in text]

lst=[]
s=0
count=0

while True:
    
    for i,j in zip(text,lengths):
        s+=j
        if s<=n:
            lst.append(i)
            count+=1
            s+=1
        else:
            if len(lst)==1:
                print(lst[0]+' '*(n-len(lst[0])))
                s=j
                lst=[]
                lst.append(i)
                count+=1
            else:
                words_sum=0
                for item in lst:
                    words_sum+=len(item)
                each_space=(n-words_sum)//(len(lst)-1)
                extra=n-(each_space*(len(lst)-1))-words_sum
                c=1
                for item in lst:
                    if c==1:
                        print(item+' '*(each_space), end='')
                        if c<=extra:
                            print(' ', end='')
                        c+=1
                    elif c==len(lst):
                        print(item)
                    else:
                        print(item+' '*each_space, end='')
                        if c<=extra:
                            print(' ', end='')
                        c+=1
                s=j
                lst=[]
                lst.append(i)
                count+=1
    if count==len(text):
        c=1
        words_sum=len(lst)-1
        for item in lst:
            if c!=len(lst):
                print(item, end=' ')
                words_sum+=len(item)
                c+=1
            else:
                words_sum+=len(item)
                tspace=n-words_sum
                print(item+' '*(tspace))
        break