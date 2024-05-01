
n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
         print("*",end="")
    print()

n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print(chr(65+k),end="")
    print()

n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

n=int(input("Enter a number"))
for i in range(n,0,-1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
#list
li = [100, 200, 300, 400, 500]
print(li[1])
print(li[-1])
print(li[::-1])
print(type(li))

li1 = [100, 200, 300, 400, 500]
li2 = [100, 1200, 300, 600, 900]
li3=li1+li2
print(li3)

li1 = [1,2,3,4,5,6,7,8,9,12]
li2=[]
for i in range(len(li1)):
    p=li1[i]*li1[i]
    li2.append(p)
print("The Squares are :",li2)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = []
for i in list1:
    for j in list2:
        result.append(i+j)
print(result)

i = [10, 20,50,60,30, 40]
i.insert(4,70)
print(i)


