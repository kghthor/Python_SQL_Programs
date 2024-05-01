'''dict1={
    "Name:" : "Harish K G",
    "Age:": 21,
    "Qualfication":"BE Graduate"
}
print(dict1)
dict2={
    "Name:" : "Harish K G",
    "Age:": 21,
    "Age:":22,#no duplicate print the updated value
    "Qualfication":"BE Graduate",
    "subject":["maths","science","chemistry"]
}
print(len(dict2))
print(dict2["subject"])
print(dict2.get("subject"))
dict3=dict(name="John",age=36,country="India")
print(dict3)
print(dict2.keys())
print(dict2.values())
dict2["IP"]=954548
print(dict2)
print(dict2.items())
print("Age:"in dict2)
dict2.update({"Name":"Dilshan"})
print(dict2)
s={
    "class":
        {"student":
             {"name":"Harish",
                  "marks":
                      {"phy":70,
                       "his":80
                       }
              }
         }
    }
print(s["class"]["student"]["marks"]["his"])
a=["Ten","Twenty","Thirty"]
b=[10,20,30]
c={}
for i in range(len(a)):
    c.update({a[i]:b[i]})
print(c)   
#x=zip(a,b)
#print(x)
#r=dict(x)
#print(r)'''
#Merge
dict1={
    "Name:" : "Harish K G",
    "Age:": 21,
    "Qualfication":"BE Graduate"
}
dict2={
    "Name1:" : "Razon K G",
    "Age1:": 22,
    "Qualfication1":"BE Graduate"
}
dict1.update(dict2)
print(dict1)
print("BE Graduate" in dict2.values())
#sum & multipy
dict1={
    "a:" : 2,
    "b:": 21,
    "c:":3
}
total=sum(dict1.values())
print(total)
b=1
for i in dict1.values():
    b*=i
print(b)    
#print work
a=15
b={}
for i in range(1,a+1):
    b.update({i:i*i})
print(b)
#Create dictionary
string = "python is a interpreted and dynamic programming language"
words = string.split()
result = {}
for word in words:
    first = word[0]
    if first in result:
        result[first].append(word)
    else:
        result[first] = [word]
print(result)


