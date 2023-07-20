import pickle
roll = input('Enter roll number whose name you want to update in binary file :')
file = open("student.dat", "wb+")
list = pickle.load(file)
found = 0
lst = [ ]
for x in list:
 if roll in x['roll']:
     found = 1
     x['name'] = input('Enter new name: ')
     lst.append(x)
if found == 1:
 file.seek(0)
 pickle.dump(lst, file)
 print("Record Updated")
else:
 print('roll number does not exist')
file.close( )
