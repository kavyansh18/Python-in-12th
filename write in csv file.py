import csv
f=open('k.csv','w')
writer_object=csv.writer(f)
header=['Roll no.','Name','Marks']
rows=[[1,'kavyansh',100],[2,'Bhanu',80]]
writer_object.writerows(header)
writer_object.writerows(rows)
f.close()
