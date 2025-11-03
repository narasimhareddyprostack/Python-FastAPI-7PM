#WAP to reprent KeyError
student={
    's_id':101,
    'name':'Rahul',
    'email':'rahul@pm.com'
}
#how to read dict values
#What is dict?
#group of key:value pair as one enity.

#how to read dict values- keys?
print(student)
print(student['s_id'])  #101 
print(student['name'])  #Rahul
print(student['email']) #rahul@pm.com

print(student['grade']) #KeyError: