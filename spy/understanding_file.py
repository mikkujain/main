import csv
file=open("file.csv.csv","r")
#print("The name of the file %s" %file.mode)
read_object=csv.reader(file)
counter=1
for row in read_object:
	if counter > 0:
		print(row)
	counter +=1
#print(str1)
file.close()