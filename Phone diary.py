f = open('phonenumber.txt', 'r')
number=[]
content=f.read()
name=input('Enter the name of person whoose phone no. is to be found: ')
lenght=len(name)
if name not in content:
  print("NO DATA AVAILABLE!")
else:
  index=int(content.index(name))
  for digit in content[index+1+lenght:index+11+lenght]:
    number.append(digit)
  print('Phone no. of ',name,'is: ',end='')
  for digit in number:
    print(digit,end='')
f.close()