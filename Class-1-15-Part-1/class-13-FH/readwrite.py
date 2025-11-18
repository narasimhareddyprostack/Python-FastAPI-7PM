fp1=open('data.txt','r')
fp2=open('abc.txt','w')
data=fp1.read()
fp2.write(data)
print("New file - abc.txt created successfully")

#resource management
fp1.close()
fp2.close()
