#####3 big number
"""a=int(input("Enter 1: "))
b=int(input("Enter 2: "))
c=int(input("Enter 3: "))
if(a>b and a>c):
	print(a,"is Greater")
elif(b>a and b>c):
	print(b,"is Greater")
else:
	print(c,"is Greater")"""
######################################
'''a=int(input("Enter a Salary :"))
if(a<10000):
	d=(a*0.25 + a*0.3) 
	net=(a+d)-a*0.08
	print(net)
elif(a>=10000 and a<20000):
	d=(a*0.2 + a*0.25) 
	net=(a+d)-a*0.06
	print(net)
elif(a>=20000 and a<30000):
	d=(a*0.15 + a*0.15) 
	net=(a+d)-a*0.02
	print(net)
else:
	d=(a*0.1 + a*0.15) 
	net=(a+d)-a*0.27
	print(net)'''
######################################
#Write a program to find the roots of a quatratic condition

import math
a=int(input("Enter the Coifficient A :"))
b=int(input("Enter the Coifficient B :"))
c=int(input("Enter the Coifficient C :"))
d=(b**2)-(4*a*c)
if(d>0):
	print(math.ceil((-b)+(d)**1/2)/2*a,math.ceil.((-b)-(d)**1/2)/2*a
#round(num,2)
elif(d==0):
	print(-b/2*a,b/2*a)
else:
	print(f"{a}+i{b},{c}+i{d}")
#grade!!
'''
a=int(input("Enter the sub1: "))
b=int(input("Enter the sub2: "))
c=int(input("Enter the sub3: "))
d=a+b+c
e=(d/300)*100
if(e>=90):
	print("The Grade is A+")
elif(e<90 and e>=80):
	print("The Grade is A")
elif(e<=70 and e>80):
	print("The Grade is B+")
elif(e<70 and e>=60):
	print("The Grade is B")
elif(e<60 and e>=50):
	print("The Grade is C")
else:
	print("Fail")'''







