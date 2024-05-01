import mysql.connector
try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="2001" ,
    )
    mycursor=mydb.cursor()
    mycursor.execute("create database contacts")
except:
        print("Already created Database")
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="2001" ,
        database="contacts",
    )
mycursor=mydb.cursor()
mycursor.execute("create table if not exists itemss(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone_number VARCHAR(200))")

def insert_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    sql = "insert into itemss (name, phone_number) VALUES (%s, %s)"
    values = (name, phone_number)
    mycursor.execute(sql,values)
    print("Contact inserted successfully.")
def update_contact():
    contact_id = input("Enter the ID of the contact to update: ")
    new_name = input("Enter the new name: ")
    new_phone_number = input("Enter the new phone number: ")
    sql = "UPDATE itemss SET name = %s, phone_number = %s WHERE id = %s"
    values = (new_name, new_phone_number, contact_id)
    mycursor.execute(sql,values)
    mydb.commit()
    print("Contact updated successfully.")
def delete_contact():
    contact_id = input("Enter the ID of the contact to delete: ")
    sql = "DELETE FROM itemss WHERE id = %s"
    values = (contact_id,)
    mycursor.execute(sql,values)
    mydb.commit()
    print("Contact deleted successfully.")  
while True:
    print("Options:")
    print("1. Insert a contact")
    print("2. Update a contact")
    print("3. Delete a contact")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        insert_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        
