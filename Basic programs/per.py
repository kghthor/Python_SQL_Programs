#Perfect or Not
n=int(input("Enter a Number :"))
s=0
i=1
while(i<=n//2):
	if(n%i==0):
		s+=i
		print(i)
	i+=1
if(s==n):
	print("Perfect")
else:
	print("Not an Perfect")
