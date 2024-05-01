###########Program to print first n natural number###############
'''n=int(input("Enter a number :"))
for x in range(1,n+1):
	print(x)'''
###########even num ###########################
'''n=int(input("Enter a number :"))
for x in range(2,n+2,2):
	print(x)'''
###########sum of first n natural number#####################
'''n=int(input("Enter a number :"))
d=0
for x in range(1,n+1):
	d+=x
print(d)'''
###########################all the factors
'''n=int(input("Enter a number :"))
for x in range(1,n+1):
	if(n%x==0):
		print(x)'''
#######################sum of factors of  number###########
''''n=int(input("Enter a number :"))
d=0
for x in range(1,n+1):
	if(n%x==0):
		d+=x
print(d)'''
###########Factorial of number####################
'''n=int(input("Enter a number :"))
d=1
for x in range(n,1,-1):
	d*=x	
print(d)'''
#############sum of even numbers upto n#################
'''n=int(input("Enter a number :"))
d=0
for x in range(2,n+2,2):
	d+=x
print(d)'''	
#################sum of odd numbers upto n#################
'''n=int(input("Enter a number :"))
d=0
for x in range(1,n+1,2):
	d+=x
print(d)'''
#perfect or not!
'''n=int(input("Enter a number :"))
d=0
for x in range(1,n//2+1):
	if(n%x==0):
		d+=x
if(d==n):
	print("perfect")
else:
	print("Not Perfect")'''


