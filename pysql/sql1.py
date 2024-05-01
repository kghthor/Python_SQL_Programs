import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001" ,
    database="mydatabase"
)
#print(mydb)
mycursor=mydb.cursor()
#mycursor.execute("create database mydatabase")
#mycursor.execute("create table customers (id int auto_increment PRIMARY KEY, name varchar (255), address varchar (255))")
'''mycursor.execute("show tables")
for x in mycursor:
    print(x)
sql="insert into customers (name,address) values (%s,%s)"
val=("Harish","Highway bro 45")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"Records inserted.")'''
'''sql = "INSERT INTO customers (name, address) VALUES (%s,%s)"
val = [
('peter','key'),
('amy','bill'),
('michael','lolty'),
('Harish','me'),
('rena','you')
]
mycursor.executemany(sql, val)
mydb.commit ()
print (mycursor.rowcount, "was inserted.")'''
'''mycursor.execute("select * from customers")
#result1=mycursor.fetchall()
result2=mycursor.fetchone()
print(result2)
#clsprint(result1)
for i in result1:
    print(i)'''
'''s="select * from customers where address='Highway bro 45'"
mycursor.execute(s)
r=mycursor.fetchall()
for i in r:
    print(i)'''
'''s="select * from customers where address like '%key'"
mycursor.execute(s)
rt=mycursor.fetchall()
for i in rt:
    print(i)'''
'''s="select * from customers order by name"
mycursor.execute(s)
ti=mycursor.fetchall()
for i in ti:
    print(i)'''
'''s="delete from customers where address='key'"
mycursor.execute(s)
tio=mycursor.fetchall()
for i in tio:
    print(i)'''