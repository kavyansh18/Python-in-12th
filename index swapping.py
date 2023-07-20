s=m=n=0
for i in (0,15):
    if i%2==0:
        s+=1
    elif i%5==0:
        m+=1
    else:
        n+=1
print(s,m,n)
