#Palindrome or Not
n=int(input("Enter a number:"))
temp=n
c=0
while n!=0:
    num=n%10
    c=c*10+num
    n=n//10
if temp==c:
    print("Palindrome")
else:
    print("Not An Palindrome")
#cube of numbers
'''n=int(input("Enter the Number:"))
for x in range(0,n+1):
    print(x**3)'''
#Factors of A number
'''n=int(input("Enter A number:"))
for x in range(1,n+1):
    if n%x==0:
        print(x)'''
#Except Multiple of three upto 20 or upto User input
'''n=int(input("Enter A number:"))
for x in range(1,n+1):
    if x%3==0:
        continue
    print(x)'''
#Except 3 and 6
'''n=int(input("Enter A number:"))
for x in range(1,n+1):
    if x==3 or x==6:
        continue
    print(x)'''
            
                    
                        
