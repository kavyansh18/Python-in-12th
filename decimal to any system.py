k=[]
n=int(input('Enter the number: '))
x=int(input('Enter the base value of converted system: '))
while n>=x:
  k.append(n%x)
  n//=x
k.append(n)
k.reverse()
for i in k:
  print(i,end="")