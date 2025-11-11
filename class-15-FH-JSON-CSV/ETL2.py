import requests,json,csv

#Extract Data from Rest API
resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()

#Transorm based on requirement
#uid,uname,email,city
user_json_data=[]
user_csv_data=[]
for user in users:
    user_json_data.append({"uid":user['id'],
                           "uname":user['username'],
                           "email":user['email'],
                           "city":user['address']['city']})
    user_csv_data.append((user['id'],
                          user['username'],
                          user['email'],
                          user['address']['city']))


#Load
#a)load into new json file - users.json
#b)load into new csv file - users.csv

fp1=open('users.json','w')
json.dump(user_json_data,fp1)
print("New JSON File Created Successfully!")


fp2=open("users.csv",'w',newline="")
csv_writer=csv.writer(fp2)
csv_writer.writerow(['uid','uname','email','city'])
csv_writer.writerows(user_csv_data)
print('New CSV File Created Successfully')
fp1.close()
