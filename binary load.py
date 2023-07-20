import pickle
f=open('data.dat','rb')
try:
    while True:
        record=pickle.load(f)
        print(record)
except:
    pass

