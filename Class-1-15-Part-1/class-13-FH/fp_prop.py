fp1=open('data.txt')
fp2=open('abc.txt','w')
#print all file properites
'''
file name 
mode 
is readble or not 
is writable or not
is closed or not
'''
print(fp1.name)   #data.txt
print(fp1.mode)   #r
print(fp1.writable()) #False
print(fp1.readable()) #True
print(fp1.closed)     #False
fp1.close()
print(fp1.closed)     #True