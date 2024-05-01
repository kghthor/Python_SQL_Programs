'''x="banana"
for i in x:
    print(i,end=" ")
print()'''
#Space as length!
'''y="Hello world!"
print(len(y))
x="My name is harish"
print("name" in x)
print("name" not in x)
print(x[2:5])
print(x[2:])
print(x[:5])
print(x[::-1])
print(x[-5:-3])
print(x.upper())
print(x.lower())
x=" My name is harish "
print(x.strip())
print(x.replace("h","b"))
x="My ,name, is, harish"
print(x.split(","))
x="My name is harish"
print(x.split("a"))
quantity=3
itemno=567
price=49.95
myorder="I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,price))
myorder1=f"I want {quantity} pieces of item {itemno} for {price} dollars"
print(myorder1)
x='T27my"name"is HARISH.'
print(x)
print(x.capitalize())
print(x.casefold())
y="babaaaa"
print(y.center(20,"*"))
print(y.count('a',3,4))
print(x.endswith("a"))
txt="harish123"
print(txt.isalnum())
a="Hello world"
b="hello 123"
c="mynameisHaris"
print(b.islower())
x="HELLO world 1234"
lower=0
upper=0
digit=0
space=0
for i in range(len(x)):
    if(x[i].islower()):
        lower+=1
    elif(x[i].isupper()):
        upper+=1
    elif(x[i].isdigit()):
        digit+=1
    elif(x[i]== " "):
         space+=1
print("Lower Case",lower)
print("Upper Case",upper)
print("Digit",digit)
print("Space",space)
#################
n=input("Enter the Sentence to split the word")
for i in range(" "):
    print(i)
txt="Hello Sam"
print(txt.maketrans("S","p"))
texty="Python is simple and oops"
b=texty.split()
print(b)
d="*".join(b)
print(d)'''
#Caps Interchange
'''x=input("Enter a String: ")
y=""
for i in x:
    if(i.islower()):
        y+=i.upper()
    elif(i.isupper()):
        y+=i.lower()
    elif(i==" "):
        y+=i
print(y)
#sort Letters
x=input("Enter a String: ")
y=""
z=""
for i in x:
    if(i.islower()):
        y+=i
    elif(i.isupper()):
        z+=i
print(z+y)
#remove
Hlist1 = ["hii", "", "hello", "lilly", "", "Be", "",""]
new=[]
for i in Hlist1:
    if(i!=""):
        new.append(i)      
print(new)
#COUNT
x=input("Enter a String: ")
vow=0
cons=0
vowels="aeiouAEIOU"
for i in x:
    if(i in vowels):
        vow+=1
    else:
        cons+=1
print(vow)
print(cons)
#Cont
x=input("Enter a String: ")
lower=0
upper=0
digit=0
special=0
for i in range(len(x)):
    if(x[i].islower()):
        lower+=1
    elif(x[i].isupper()):
        upper+=1
    elif(x[i].isdigit()):
        digit+=1
    elif(x[i]!= " "):
         special+=1
print("Lower Case",lower)
print("Upper Case",upper)
print("Digit",digit)
print("Special",special)'''
#Caps Title
'''x=input("Enter a String: ")
print(x.title())'''

