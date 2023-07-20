k1=0
k2=0
x=int(input('Enter the base value: '))
n=eval(input('Enter the number: '))
n1=str(int(n//1))
n2=str(str(n)[(len(n1)+1)::])
l1=len(n1)-1
l2=-1
for i in n1:
  s1=int(i)*(x**l1)
  k1+=int(s1)
  l1-=1
for i  in n2:
  s2=int(i)*(x**(l2))
  k2+=(s2)
  l2-=1
f=0
f+=k1
f+=k2
print(f)
