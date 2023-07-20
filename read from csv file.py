import csv
f=open('k.csv','r')
reader_object=csv.reader(f)
h=next(reader_object)
for i in reader_object:
    print(i)
f.close()
