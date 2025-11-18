#import required modules
import requests,csv,json,mysql.connector,pymongo

#Extract 
prod_resp=requests.get('https://dummyjson.com/products')
products=prod_resp.json()['products']
#print(type(products))

#Traform - only beauty products
beauty_products_csv_mysql=[]
beauty_products_json_mongo=[]
for product in products:
    if product['category'] == "beauty":
        beauty_products_csv_mysql.append((product['id'],
                                          product['title'],
                                          product['price'],
                                          product['category'],
                                          product['rating']))
        
        beauty_products_json_mongo.append({"pid":product['id'],
                                           "pname":product['title'],
                                           "price":product['price'],
                                           "category":product['category'],
                                           "rating":product['rating']})

#print(beauty_products_csv_mysql)
#print(beauty_products_json_mongo)


#Load into CSV
fp1=open('beauty.csv','w',newline="")
cw_obj=csv.writer(fp1)
cw_obj.writerow(["pid","pname","price","category","rating"])
cw_obj.writerows(beauty_products_csv_mysql)
print("New CSV File Created Successfully")

#Load into JSON file 
fp2=open('beauty.json','w')
json.dump(beauty_products_json_mongo,fp2)
print("New JSON File Created!")

#load mongo DB
client=None 
try:
    client=pymongo.MongoClient('mongodb://localhost:27017/') 
    db=client['db6']
    product_col=db['products']
    product_col.insert_many(beauty_products_json_mongo)
    print("Data Inserted successfully!")

except:
    print("Unable Inserted") 


#load into Mysql product table
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="db6")
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
            insert into products(pid,pname,price,category,rating)
            values(%s,%s,%s,%s,%s)
           '''
    cursor.executemany(sql_st,beauty_products_csv_mysql)
    dbcon.commit()
    print("Data Inserted Successfully into Mysql Table")
    
except mysql.connector.Error as err:
    print(err) 
