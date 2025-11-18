import requests,json,csv

#Extract Data from Rest API
resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
status_code=resp.status_code

print(users)
print(status_code)