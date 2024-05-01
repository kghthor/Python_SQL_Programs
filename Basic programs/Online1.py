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
n=int(input("Enter a NUmber:"))
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
print("The sum is :",sum)
