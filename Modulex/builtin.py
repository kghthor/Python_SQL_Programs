'''import math
#import math as m ->easy use
#from math import pi -> what we need to import less space coverage
print("value of pi",round(math.pi))
print(dir(math))#Fuctions Inside the component
print(math.factorial(5))
import datetime
a=datetime.datetime.now()
print(a)
print(dir(datetime.datetime))
print(datetime.date.today())
k=datetime.date(2023,12,21)
t=datetime.date.today()
print(t.year)
print(t.month)
print(t.day)'''
'''import datetime
a=datetime.time()
b=datetime.time(11,24,56,545564)
print(a)
print(b)
s=datetime.now()
t=s.strftime("%H:%M:%S")
print(t)'''
'''from datetime import datetime
d="21 June,2018"
do=datetime.strptime(d,"%d %B,%Y")
print("do=",do)
import random
num=random.random()
num1=random.randint(0,123123)
print(num)
print(num1)
r=random.choice("Random Module")
print(r)
k=random.choice([34,6,23,33,333])
print(k)
lid=[233,534,34,34]
random.shuffle(lid)
print(lid)'''
