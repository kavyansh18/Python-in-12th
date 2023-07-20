l=[4,20,9,78,45,34,76,56]
print(l)
if len(l)>4:
    for i in range(2):
        k=l.pop(0)
        l.append(k)
    for i in range(2):
        s=l.pop(-3)
        l.insert(0,s)
else:
    print('inappropriate lenght')
print(l)
    
