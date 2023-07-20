def INDEX_LIST(L):
    indexlist=[]
    for i in L:
        if i==0:
            indexlist.append(L.index(i))
    print('The indexList will have -',indexlist)
L=[0,4,0,11,0,56]
INDEX_LIST(L)
