while True:
    l=[0,1,2,3,4,5,6,7,8,9]
    s=0
    x=input('Enter your phone number: ')
    if len(x)!=10:
        s+=1
    for i in x:
         if int(i) not in l:
            s+=1
    if s==0:
        print('CORRECT INPUT')
        break
    else:
        print('INVALID')
