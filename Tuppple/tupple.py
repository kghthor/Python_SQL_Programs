tuple1="abc",
tuple2="abc"
tuple3="one",1,"fruits"
tuple4=(1,"abc",2,"apple")
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))
print(tuple4[1])
tuple5=tuple3+tuple4
print(tuple5)
tuple6=(0,1,2,3)
tuple7=('python','pro')
tup=(tuple6,tuple7)
print(tup)
if(1 in tuple3):
    print("Present")
else:
    print("No")

tu=("Pytons","dragons")*3
print(tu)

'''tuple4[2]="king"
del tuple4[1]
print(tuple4)

tuple4.append(5)
tuple4.remove("abc")'''

list1=list(tuple5)
del list1[1]
list1.append("Harish")
list1.insert(3,5)
list1.remove("one")
tu1=tuple(list1)
print(tu1)
a,b,c,d,e,f,g=tu1
print(a,b,c,d,e,f)
#we can use * operator(univeral operator)#ask
print(tu1.count(2))
tups1=1,2,3,45,6,
su=sum(tups1)
print(su)
print(len(tu1))
print(max(tups1))
print(min(tups1))
print(tups1.index(45))
#print(tups1.index(67))
for i in tups1:
    print (i)

for i in range(len(tups1)):
    print(tups1[i])
a="harish","willam","Saji"
b="chennai","kollam","coimbatore"
c=455,56,66
d=zip(a,b,c)
print(list(d))
print(sorted(c),reverse="true")
