f=open('textfile.txt','r')
k=0
r=0
l=[]
c=f.readlines()
for i in c:
    p=i.split()
    if p[0].lower() in ['a','an','the']:
        k+=1
        l.append(r)
    r+=1
print('No. of lines: ',k)
for i in l:
    print(c[i])
f.close()
