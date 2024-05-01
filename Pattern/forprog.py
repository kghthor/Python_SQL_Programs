#21/07/23
#10 Table print
'''n=int(input("Enter the number"))
for i in range(1,n+1):
    print(i,'*',n,'=',n*i)'''            
#even
'''sum=0
for i in range(30):
    if(i%2==0):
        sum+=i
print(sum)'''
#cube upto 5
'''cube=0
for i in range(1,6):
   cube+=i**3
print(cube)'''
#factorial
'''n=int(input("Enter a number :"))
d=1
for x in range(n,1,-1):
	d*=x	
print(d)'''
#Fibannonci Seris#sum of that
'''n=int(input("Enter a NUmber:"))
first = 0
second = 1
print(first)
print(second)
sum=1
for x in range(3,n+1):
    third = first + second
    sum+=third
    print(third)
    first,second=second,third
print("The sum is :",sum)'''
#22/07/23
#Simple calculator
'''print("Choose 1 for add")
print("Choose 2 for sub")
print("Choose 3 for mul")
print("Choose 4 for div")
n=int(input("Enter the Function: "))
a=int(input("Enter a Number 1:"))
b=int(input("Enter a Number 2:"))
if(n==1):
    print(a+b)
elif(n==2):
    print(a-b)
elif(n==3):
    print(a*b)
else:
    print(a/b)'''
#Nested For(Tables)
'''n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range (1,n+1):
        print(i,"*",j,"=",i*j,end=" ")
    print( )'''
#pattern(Empty Square)
'''n=int(input("Enter the number:"))
for i in range(n):
    for j in range (n):
            if i==0 or j==0 or j==n-1 or i==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()'''
#pattern #set for both  odd num & even:(+)
'''n=int(input("Enter the number:"))
for i in range(n):
    for j in range (n):
            if(n%2!=0):  
                if i==n//2 or j==n//2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            else:
                if i==n//2-1 or j==n//2-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")         
    print()'''
##########################################odd num & even(T)
'''n=int(input("Enter the number:"))
for i in range(n):
    for j in range (n):
            if(n%2!=0):  
                if i==0 or j==n//2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            else:
                if i==0 or j==n//2-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")         
    print()'''
#####################################(X)
'''n=int(input("Enter the number:"))
for i in range(n):
    for j in range (n):
                    if i==j or i+j==n-1:
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
    print()'''
#31/07/2023##########################################triangle str 
'''n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()'''
####################### Table traingle-> when i is in 0 no execution when (n+1)is given######
'''n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()'''
##################################################
'''n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end=" ")
    print()'''
    
