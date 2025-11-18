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
            insert into users values(101,'Rahul','rg@gmail.com','Bangalore');
           ''' 
    
    cursor.execute(sql_st)
    dbcon.commit()
    print("Inserted Successfully")
except mysql.connector.Error as err:
    print(err)

finally:
    pass
