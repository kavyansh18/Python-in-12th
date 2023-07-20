f=open('textfile.txt','r')
k=f.read().split()
l=[]
for i in k:
    l.append(k.count(i))
s=l.index(max(l))
print(k[s])
print(max(l))
