import pickle
f=open('student.dat','rb')
try:
  while True:
    data=pickle.load(f)
    print(data)
except:
  pass
f.close()
  

