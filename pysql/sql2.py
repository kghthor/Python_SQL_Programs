import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001" ,
    database="Family" 
)
mycursor=mydb.cursor()
#mycursor.execute("create database Family")
#mycursor.execute("create table mem (id int auto_increment PRIMARY KEY, Name varchar (255), Address varchar (255),Realtion varchar(255),Age int,Designation varchar(255))");
sql = "INSERT INTO mem (name, address,realtion,age,designation) VALUES (%s,%s,%s,%s,%s)"
val = [
('Kala','Coimbatore','Aunt','45','Teacher'),
('amy','Chennai','Uncle','55','IAS'),
('michael','Ooty','Brother','22','Business man'),
('Harish','New Delhi','Me','21','prime Minsister'),
('rena','US','Sister','23','It')
]
mycursor.executemany(sql,val)
mydb.commit()
print (mycursor.rowcount, "was inserted.")
#####################################################3
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