import mysql.connector
dbcon=None 
cursor=None 

try:
    dbcon=mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="db6")
    cursor=dbcon.cursor()
    sql_st='''
            insert into users(uid,uname,email,city) 
            values(%s,%s,%s,%s);
           ''' 
    employees=[
        (102,'Sonia','sg@gmail.com','ND'),
        (103,'Priya','pg@gmail.com','ND'),
        (104,'Modi','modi@gmail.com','Chennai')
    ]
    cursor.executemany(sql_st,employees)
    dbcon.commit()
    print("Inserted Successfully")
except mysql.connector.Error as err:
    print(err)

finally:
    cursor.close()
    dbcon.close()
