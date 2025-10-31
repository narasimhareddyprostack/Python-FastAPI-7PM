#create
emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000
}
#read
print(emp) 
#how to read dict values - using key
print(emp['eid'])   #101
print(emp['ename']) #Rahul
print(emp['esal'])  #45000
#print(emp['loc'])   #KeyError: 'loc'

#update
emp['esal'] = 55000
print(emp)

#delete
del emp['esal']
print(emp)  {'eid': 101, 'ename': 'Rahul'}