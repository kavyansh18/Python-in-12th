import pickle
f=open('student.dat','rb')
key=int(input('Enter the roll no. to search: '))
try:
  while True:
    data=pickle.load(f)
    if data['roll no.']==key:
     print(data)
except:
  pass
f.close()


  

