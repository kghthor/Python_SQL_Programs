'''class harish:
    x=5#inside class
z=harish()#outside class
print(z.x)
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfuc(self):
        print("Hello"+self.name)
p1=person("har",36)
p1.myfuc()
p2=person("king",4)
p2.myfuc()'''
#single Inheriance
'''class animal:
    def speak(self):
        print("Speaking animal")
class Dog(animal):
    def bark(self):
        print("dog barking")
d=Dog()
#d1=Dog()
d.speak()
d.bark()'''
#multi
'''class animal:
    def speak(self):
        print("Speaking animal")
class Dog(animal):
    def bark(self):
        print("dog barking")
class child(Dog):
    def pup(self):
        print("crying")
k=child()
k.speak()
k.bark()
k.pup()
#Multiple
class cal1:
    def sum(self,a,b):
        return a+b;
class cal2:
    def mul(self,a,b):
        return a-b;
class cal3(cal1,cal2):
    def div(self,a,b):
        return a/b;
d=cal3()
print(d.sum(20,30))
print(d.mul(40,30))
print(d.div(10,20))'''
#Heriarchy
'''class parent:
    def func1(self):
        print("parent class")
class child1(parent):
    def func2(self):
        print("child 1")
class child2(parent):
    def func3(self):
        print("child 2")
obj1=child1()
obj2=child2()
#print(issubclass(child1,parent))
#isinstance
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()
#hybrid inheritance->covers more than 1 type'''
'''class parent:
    def func1(self):
        a=10
        b=90 
        c=a+b
        print(c)
        print("ADDITION")
class child1(parent):
    def func2(self):
        a=10
        b=90 
        c=a*b
        print(c)
        print("MULTIPLICATION")
class child2(parent):
    def func3(self):
        a=10
        b=90 
        c=a-b
        print(c)
        print("SUBTRACTION")
obj1=child1()
obj2=child2()
obj1.func1()
obj1.func2()
#obj2.func1()
obj2.func3()
class vehicle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def func1(self):
        print("Name:",self.a)
        print("Speed",self.b)
        print("Capacity",self.c)
class bus(vehicle):
     def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
     def func1(self):
        print("Name:",self.a)
        print("Speed:",self.b)
        print("Capacity:",self.c)
        super().func1()
#k=vehicle("benz",456,5)
#k.func1()
d=bus("king",54,5)
d.func1()
########
class harish:
    d=465
    def me(self):
        a=10 
        b=20
        print(a,b)
di=harish()
di.me()
print(di.d)'''
#Home Work
'''class student:
    def __init__ (self,nme,r,a,b,c):
        self.name=nme
        self.rollno=r 
        self.m1=a
        self.m2=b
        self.m3=c
        self.total=0
    def calculate(self):
        self.total=self.m1+self.m2+self.m3
    def check_grade(self):
        self.per=int((self.m1+self.m2+self.m3)*100/300)
        if self.m1>=50 and self.m2>=50 and self.m3>=50:
            if self.per>=90:
                self.grade="A+"
            elif self.per>=80:
                self.grade="A"
            elif self.per>=70:
                self.grade="B+"
            elif self.per>=60:
                self.grade="B"
            else:
                self.grade="C"
        else:
            self.grade="Failed"
    def display(self):
        print("Name      :",self.name)
        print("Roll No   :",self.rollno)
        print("Phyics    :",self.m1)
        print("Chimstry  :",self.m2)
        print("Maths     :",self.m3)
        print("Total     :",self.total)
        print("percentage:",self.per)
        print("Grade     :",self.grade)
        print("---------------------------------------")
list=[]
n=int(input("Enter the number of students :"))
for i in range(0,n):
    nme=input("Enter the Name :")
    rno=int(input("Enter the Roll no:"))
    x=int(input("Physics mark:"))
    y=int(input("Chimstry mark:"))
    z=int(input("Maths Mark:"))
    s=student(nme,rno,x,y,z)
    s.calculate()
    s.check_grade()
    list.append(s)##see this s 
for i in list:
    i.display()
print("Name\tRollNo\tTotal\tPerct\tGrade")
for i in range(0,n):
    print(list[i].name,"\t",list[i].rollno,"\t",list[i].total,"\t",list[i].per,"\t",list[i].grade)'''
class bank:
    def __init__(self,name,acct_no):
        self.name=name
        self.acct_no=acct_no   
        self.balance=0
    def display(self):
        print("Acc Details")
        print("-------------")
        print("Acc holdder",self.name)
        print("Acc num",self.acct_no)
    def deposit(self,deposit):
        self.balance=self.balance+deposit
        print("Deposit Sucessfully")
        print()
    def withdraw(self,w):
        if w<self.balance:
            self.balance=self.balance-w
            print("Amount Withdrawed")
        else:
            print("Not enough Balance")
    def balance1(self):
        return self.balance
name=input("Enter the acc")
acct_no=int(input("Enter the no"))
s=bank(name,acct_no)
s.display()
print("1.Deposit")
print("2.Withdraw")
print("3.View Balance")
print("4.Exit")
while(True):
    print()
    n=int(input("Enter the choice"))
    if n==1:
        deposit=int(input("Deposit amount :"))
        s.deposit(deposit)
    elif n==2:
        wdraw=int(input("Amount Withdraw"))
        s.withdraw(wdraw)
    elif n==3:
        print("Balance is",s.balance1())
    elif n==4:
        print("Exit")
        break
    else:
        print("Wrong Choice")