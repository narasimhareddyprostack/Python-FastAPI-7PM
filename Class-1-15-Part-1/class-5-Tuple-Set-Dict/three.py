#create
unames=("Rahul","Sonia","Priya","Modi")
#index   0        1      2       3
print(type(unames))

#read
print(unames)
#how to read tuple elements - using index 
print(unames[0]) #Rahul

#update
unames[0] = "Rahul Gandi"  
#TypeError: 'tuple' object does not support item assignment
#List is Mutalbe Object - we can perfrom update and delete o
#Tuple is Immutalbe Object - Tuple is read only version of list