import mysql.connector

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
            create table users(
            uid int,
            uname varchar(32),
            email varchar(50),
            city varchar(32)
            )
           '''
    cursor.execute(sql_st)
    print("New Table Created")

except mysql.connector.Error as err:
    print(err)

finally:
    cursor.close()
    dbcon.close()