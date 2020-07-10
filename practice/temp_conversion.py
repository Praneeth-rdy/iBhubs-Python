def main(temp):
    # update logic here
    if(temp[-1]=='C'):
        c=float(temp[:-1])
        C=str(round(c,2))+'C'
        f=(9/5)*c+32
        F=str(round(f,2))+'F'
        k=c+273
        K=str(round(k,2))+'K'
        return [C,F,K]
    elif(temp[-1]=='F'):
        f=float(temp[:-1])
        F=str(round(f,2))+'F'
        c=(f-32)*5/9
        C=str(round(c,2))+'C'
        k=c+273
        K=str(round(k,2))+'K'
        return [C,F,K]
    else:
        k=float(temp[:-1])
        K=str(round(k,2))+'K'
        c=k-273
        C=str(round(c,2))+'C'
        f=(9/5)*c+32
        F=str(round(f,2))+'F'
        return [C,F,K]


temp = input()

print(main(temp)[0]+'\n'+main(temp)[1]+'\n'+main(temp)[2])