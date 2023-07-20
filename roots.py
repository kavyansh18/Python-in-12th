def root(a,b,c):
  d=(b**2)-4*a*c
  r1=(-b+d**(1/2))/2*a
  r2=(-b-d**(1/2))/2*a
  print("roots are",r1,r2)
  if d==0:
    print("roots are real and equal")
  elif d>0:
   print("roots are real and unequal")
  elif d<0:
   print("roots are imaginary")

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: ")) 
root(a,b,c)