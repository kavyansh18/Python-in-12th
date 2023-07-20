while True:
    x=input('Enter your email: ')
    if '@'not in x or '.' not in x or x.index('@') > x.index('.'):
        print('INVALID INPUT!')
    else:
        print('CORRECT INPUT')
        break
