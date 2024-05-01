import mysql.connector
try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="2001" ,
    )
    mycursor=mydb.cursor()
    mycursor.execute("create database exstud")
except:
        print("Already created Database")
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="2001" ,
        database="exstud",
    )
mycursor=mydb.cursor()
mycursor.execute("create table if not exists itemss(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),Class int,Marks int,Place varchar(255))")
data_to_insert = [
    ('John',12,100,'KanniyaKumari'),
    ('Jane',10,34,'Chennai'),
    ('Alice',9,22,'Namakal'),
    ('Bob', 8, 99,'Thirupur'),
    ('Eve',7,90,'Salem')
]
sql ="INSERT INTO itemss (name,class,marks,place) VALUES (%s,%s,%s,%s)"
#mycursor.executemany(sql,data_to_insert)
#mydb.commit()
#print("Records inserted successfully!")
mycursor.execute("select * from itemss")
result1=mycursor.fetchall()
for i in result1:
    print(i)
