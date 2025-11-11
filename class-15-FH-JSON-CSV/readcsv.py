#read json file emp.json and print all employee names
import csv

fp=open('emp.csv','r')
csv_reader=csv.reader(fp)
employees=list(csv_reader)

for emp in employees[1:]:
    print(emp[1])