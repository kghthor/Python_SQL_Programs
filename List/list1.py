#Basics of List
'''list1=["Harish",100,8.9,'s']
print(list1)
print(list1[0])
list1[1]='king'
del list1[2]
print(list1[1])
print(list1)
list2=[1,2,3,4,4]
print(list2*2)
print(30 in list2)
list3=[123,45,456,54]
print(max(list3))
print(min(list3))
print(list2+list3)
list4=list1+list2
print(list4)'''
'''#list4.clear()
#print(list4)
print(len(list1))
a="Thor"*4
print(a)
#b=list2+list3
#print(list3 in list2)
print(len(list2))
print(["HARISH"]*4,[1]*5,"bill "*6)
for i in range(len(list1)):
    print(list1[i])
print(list1[-1])
my_list=[1,2,3,4,5,6,7,8,9]
print(my_list[0])
print(my_list[2])
print(my_list[-1])
print(my_list[1:5:2])
print(my_list[:5])
print(my_list[5:])
print(my_list[::2])
print(my_list[::-1])
print(list2.count(4))
my_list.insert(2,"God")
my_list[3]="Me"
my_list.remove(7)
my_list.pop(8)
print(my_list)'''

'''n=int(input("Enter the limit"))
list1=[]
for i in range(0,n):
      k=int(input())
      list1.append(k)
print("The User Entered Values in list:",list1)
list2=[]
for i in range(len(list1)):
    if(list1[i]%2==0):
        list2.append(list1[i])
print("The Even numbers in the list:",list2)'''
#Nested for loop
'''list1 = ["apple", "banana","mulberry", ["cherry", ["cashew", "litchi", ["tomato", "chilli","ginger"], "grapes"], "lemon"], "mango", "orange"]
print(len(list1))
print(list1[4])
print(list1[3][1][0])
print(list1[3][1][2][1])
print(list1[3][1][2][2])
print(list1[2])
print(list1[3][2])
print(list1[3])'''

'''#Creating List
a=[2,4,0,6,1,3,7,0,9,12,0,33,77,88,99,100]
b=[]
c=[]
d=[]
for i in a:
    if(i==0):
        b.append(i)
    elif(i%2==0):
        c.append(i)
    else:
        d.append(i)
print("Zero List: ",b)
print("Even List: ",c)
print("Odd List: ",d)
#User List
n=int(input("Enter the list limit"))
list1=[]
for i in range(1,n+1):
      k=int(input())
      list1.append(k)
print("The User Entered Values in list:",list1)
list1.insert(int(n/2),100)
print("Modified list:",list1)
#Del Middle
n=int(input("Enter the list limit"))
list1=[]
for i in range(1,n+1):
      k=int(input())
      list1.append(k)
print("The User Entered Values in list:",list1)
a=int(n/2)
list1.pop(a)
print("Modified list:",list1)
#Interchange
n=int(input("Enter the list limit"))
list1=[]
for i in range(n):
      k=int(input())
      list1.append(k)
print("The User Entered Values in list:",list1)
a=list1[n-1]
b=list1[0]
list1.pop(0)
list1.pop(-1)
list1.insert(0,a)
list1.insert(n-1,b)
print("Interchanged List: ",list1)
#List Length
a=[2,4,0,6,1,3,7,0,9,12,0,33,77,88,99,100]
print("Length 1",len(a))
n=0
for i in range(len(a)):
        n+=1
print("Length 2",n)
n=0
for i in a:
    n+=1
print("Length 3",n)
#in List Exist or not
a=[2,4,0,6,1,3,7,0,9,12,0,33,77,88,99,100]
print(6 in a)
#count even or odd
n=int(input("Enter the list limit"))
list1=[]
for i in range(1,n+1):
      k=int(input())
      list1.append(k)
print("The User Entered Values in list:"),list1
count1=0
count2=0
for i in list1:
      if(i!=0):
          if(i%2==0):
              count1+=1
          else:
              count2+=1
print("Even Count:",count1)
print("Odd Count:",count2)'''
'''#Clear Elements
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)
#*************************
my_list = [1, 2, 3, 4, 5]
my_list = []
print(my_list)'''
'''#********************
#Sum of list elements
a=[2,4,0,6,1,3,7,0,9,12,0,33,77,88,99,100]
b=sum(a)
print(b)
#Average of lsit elements
a=[2,4,0,6,1,3,7,0,9,12,0,33,77,88,99,100]
b=sum(a)
c=len(a)
d=int(b/c)
print(d)
#Reversing List
a=[2,4,0,6,1,3,7,0,9,12,0,33,77,88,99,100]
print(a[::-1])
#Occurance of Element in List
n=int(input("Enter the list limit"))
list1=[]
for i in range(1,n+1):
      k=int(input())
      list1.append(k)
print("The User Entered Values in list:",list1)
count=0
s=int(input("Enter for search"))
for i in list1:
    if(s==i):
      count=count+1
print("The Searched element present",count,"time in the List")
#even numbers in list
n=int(input("Enter the list limit"))
list1=[]
for i in range(1,n+1):
      k=int(input())
      list1.append(k)
print("The User Entered Values in list:"),list1
even=[]
for i in list1:
      if(i!=0):
          if(i%2==0):
              even.append(i)
print("Even Numbers:",even)
#Positive and negative numbers
n=int(input("Enter the list limit"))
list1=[]
for i in range(1,n+1):
      k=int(input())
      list1.append(k)
print("The User Entered Values in list:"),list1
count1=0
count2=0
for i in list1:
      if(i!=0):
          if(i<0):
              count1+=1
          else:
              count2+=1
print("Negative:",count1)
print("Positive:",count2)
#Remove MUltiple Elements->>>not duplicate
list1 = [1,2,3,4,5,2,7,4,6]
remove1 = [2,4,6]
for i in remove1:
    for j in list1:
        if(i==j):
            list1.remove(i)
print(list1)
#remove Empty List
list1 = [[1, 2, 3],[],[4, 5],[],[],[6, 7, 8],[]]
a=[]
list2=[]
for i in list1:
    if i!=a:
        list2.append(i)
print(list2)
#Frequency
list1=[1,2,3,1,2,3,2,3,87,87,65,87,9,9,67,9]
list2=[]
for i in list1:
    if(i>=3):
        list1.remove(i)
print(list1)'''
#uncommon elemts        
test_list = [[4, 1, 6], [7, 8], [4, 10, 8],[2,3]]
list2=[[4, 1, 6], [7, 8], [4, 10, 8],[2,4],[3,3],[7,7],[8,9]]
list3=[]
for i in test_list:
      if i not in list2:
            list3.append(i)
for i in list2:
      if i not in test_list:
            list3.append(i)
print(list3)
#Sort
list1 = [[4, 1, 6], [7, 8], [4, 10, 8]]
c=sorted(list1)
d=[]
for i in c:
      d.append(sorted(i,reverse=True))
print(d)      
