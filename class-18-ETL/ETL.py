#import required modules
import requests,csv,json,mysql.connector,pymongo

#Extract 
prod_resp=requests.get('https://dummyjson.com/products')
product_data=prod_resp.json()
print(type(product_data))

products=product_data['products']

print(type(products))

#Traform - only beauty products