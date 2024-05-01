'''a=int(input("Enter a number: "))
i=1
while(i<=a):
	print(i,end=" ")
	i+=1'''
'''a=int(input("Enter a number: "))
b=2
while(b<=a):
	print(b)
	b+=2'''
#odd
'''a=int(input("Enter a number: "))
b=1
while(b<=a):
	print(b,end=" ")
	b+=2'''
#sum!
'''n=int(input("Enter a number: "))
i=1
s=0
while i<=n:
	s=s+i
	i=i+1
print("sum is ",s)'''
#factorial of a number
'''a=int(input("Enter a number: "))
c=a
b=1
while(a>=1):
	b=b*a
	a-=1
print(f"The factorial of {c} :",b)'''
#Factors
'''n=int(input("Enter a number: "))
i=1
print("Factors are :")
while(i<=n):
	if(n%i==0):
		print(i)
	i+=1'''
#sum of factors
n=int(input("Enter a number: "))
i=1
s=0
print("Factors are :")
while(i<=n):
	if(n%i==0):
		s+=i
		print(i)
	i+=1
print(s)	
#reverse a number