while True:
    l=''
    s=0
    print('FORMAT DD/MM/YYYY')
    print('Canditate should be born before 2022')
    n=input('Enter the date: ')
    l+=(n[0:2])
    l+=(n[3:5])
    l+=(n[6:10])
    if l.isalnum() is False:
        s+=1
    elif int(n[3:5])>12 or  int(n[3:5])<=0:
        s+=1
    elif int(n[0:2])<=0:
        s+=1
    elif int(n[6:10])>2021 or int(n[6:10])<=0:
        s+=1
    elif int(n[3:5])==1 or int(n[3:5])==3 or int(n[3:5])==5 or int(n[3:5])==7 or int(n[3:5])==8 or int(n[3:5])==10 or int(n[3:5])==12:
        if int(n[0:2])>31:
            s+=1
    elif int(n[3:5])==4 or int(n[3:5])==6 or int(n[3:5])==9 or int(n[3:5])==11:
        if int(n[0:2])>30:
            s+=1
    elif int(n[3:5])==2:
        if int(n[6:10])%4==0:
            if int(n[0:2])>29:
                s+=1
        else:
            if int(n[0:2])>28:
                s+=1
    if s!=0:
        print('INVALID')
    else:
        print('CORRECT INPUT')
        break
            
        
    
            


        
