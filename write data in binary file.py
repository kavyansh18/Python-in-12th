import pickle
f=open('student.dat','ab')
d={}
s=int(input('Enter no. of datas to be entered: '))
for i in range(s):
  x=int(input('Enter the roll no.: '))
  y=input('Enter the name: ')
  z=int(input('Enter the marks: '))
  d['roll no.']=x
  d['name']=y
  d['marks']=z
  pickle.dump(d,f)
f.close()
  

