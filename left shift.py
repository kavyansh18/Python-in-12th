l=[40,30,20,10,90,70]
print(l)
n=int(input('Enter the number of indexes to be shifted towards left'))
l=l[n:]+l[:n]
print('Shifted list: ',l)
