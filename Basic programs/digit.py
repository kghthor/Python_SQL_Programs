'''a=int(input("enter a number:"))
s=0
while(n !=0):
	d=n%10
	s=s+d
	n=n//10
print("Sum of Digits is ",s)'''
###################################even
'''n=int(input("enter a number:"))
s=0
while(n!=0):
	d=n%10
	if(d%2==0):
		s=s+d
	n=n//10
print("Sum of even num: ",s)'''
####################################odd
'''n=int(input("enter a number:"))
s=0
while(n!=0):
	d=n%10
	if(d%2!=0):
		s=s+d
	n=n//10
print("Sum of odd num: ",s)'''
####################################Big n numbers
'''n=int(input("Enter input:"))
num=int(input("Enter the number :"))
big=num
n-=1
while(n>0):
	num=int(input("Enter the number :"))
	if(num>=big):
		big=num
	n-=1
print(big)'''
####################################Smallest n numbers
'''n=int(input("Enter input:"))
num=int(input("Enter the number :"))
big=num
n-=1
while(n>0):
	num=int(input("Enter the number :"))
	if(num<=big):
		big=num
	n-=1
print(big)'''

################################Digit in a given  number
'''n=int(input("enter a number:"))
big=0
while(n!=0):
	d=n%10
	if(d>big):
		big=d
	n=n//10
print("Bigest number: ",big)'''
#########################################smallest
###Reverse in a given  number
'''n=int(input("enter a number:"))
rev=0
while(n!=0):
	d=n%10
	rev=(rev*10)+d
	n=n//10
print(rev)'''
#########################################Palindrome!!!
'''n=int(input("enter a number:"))
c=n
rev=0
while(n!=0):
	d=n%10
	rev=(rev*10)+d
	n=n//10
if(rev==c):
	print("Palindrome")
else:
	print("Not an Palindrome")'''
##########################Amstrong
'''n=input("enter a number:")
l=len(n)
n=int(n)
s=0
t=n
while(n!=0):
	d=n%10
	s=s+d**l
	n=n//10
if(t==s):
	print("Amstrong")
else:
	print("Not an Amstrong")'''
#################Print decimal to Binary############################
'''d=int(input("enter a number:"))
b=0
i=1
#(r*(10**i)
while(d!=0):
	r=d%2
	b=b+r*i
	i*=10
	d=d//2	
print("Binary Equalient is : ",b)'''
###################Binary to Decimal#################################
'''d=int(input("enter a number:"))
b=0
i=0
while(d!=0):
	r=d%10
	b=b+r*2**i
	i+=1
	d=d//10	
print("Binary Equalient is : ",b)'''
######################################Prime or Composite################
n=int(input("enter a number:"))
if n<=1:
	i=2
	while i<=n//2:
		if n%i==0:
			print(n,"is Composite")
			break
		i=i+1
	else:
		print(n,"is prime")
else:
	print("Neither prime or Composite")
######################################################



