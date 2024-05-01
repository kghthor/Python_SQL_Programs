''''a=int(input("Enter the Employee Salary : "))
b=(a*0.1 + a*0.15)
net=(b+a)-(a*0.04)
if(a<10000):
	d=(a*0.2 + a*0.25)
	net=(d+a)-(a*0.06)
print(net)'''
a=int(input("Enter the Employee Salary : "))
if(a<10000):
	d=(a*0.2 + a*0.25)
	net=(d+a)-(a*0.06)
	print(net)
else:
	b=(a*0.1 + a*0.15)
	net=(b+a)-(a*0.04)
	print(net)