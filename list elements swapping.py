def Rearrange(l):
    x=int(len(l)/2)
    if len(l)%2==0:
        for i in range(0,x):
            l[i],l[x]=l[x],l[i]
            x+=1
    else:
        for i in range(0,x):
            l[i],l[x+1]=l[x+1],l[i]
            x+=1
    print(l)
Rearrange([1,2,3,4,5])
