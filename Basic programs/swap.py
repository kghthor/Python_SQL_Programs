'''a=int(input("Enter a number 1 :"))
b=int(input("Enter a number 2 :"))
print("The Two number Before swap 1 & 2 are : ",a,b)
c=a
a=b
b=c
print("The Two number after swap 1 & 2 are : ",a,b)'''
'''a=int(input())
lis=[]
for i in range(a):
    s=int(input())
    if(s%10==3 or s%10==6):
        lis.append(s)
print(sum(lis))'''
a=input()
count=0
for i in range(len(a)-1,-1,-1):
    if(int(a[i])%2!=0):
        count+=1
        print(a[i],end="")
if(count==0):
    print("-1")