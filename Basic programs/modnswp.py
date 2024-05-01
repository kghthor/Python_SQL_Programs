a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print("Before swap :",a,b)
#(a,b)=(b,a)
a=a^b
b=a^b
a=a^b
print("After swap :",a,b)