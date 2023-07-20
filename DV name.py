while True:
    x=input('Enter your name: ')
    for i in x:
        if i.isalpha() is False:
            print('INVALID')
            break 
    else:
        print('CORRECT INPUT')
        break
