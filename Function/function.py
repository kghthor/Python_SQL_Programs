'''def greet(name):
    print(name,'See me you know me')
greet("hello word")
greet("Ali baba")
#**********
def sq(x):
    return x*x
print(sq(5))
#********
def si(p,n,r):
    ad=p*n*r    
    q=ad/100
    return q
a=si(20,30,40)
print(a)
#*****************
def circle(r):
    radius=2*3.14*r
    cir=3.14*r*r
    print("Radius of circle: ",radius)
    print("Circumference: ",cir)
circle(7)
#**********
n=11
def table(i):
    for j in range(1,n):
        print(i,"*",j,"=",i*j)
table(5)
def student(**s):
    print("name:",s["name"])
student(name="Harish",age=22)
#Recursion
def rec(n):
    if n<=1:
        return n
    else:
        return n*rec(n-1)
#ho=rec(5)
s=int(input())
ho=rec(s)
print(ho)
#list pass
def sums(n):
    s=0
    for i in n:
        s+=i
    print(s)
num=[1,2,3,4,5,6,7,8,9,10]
sums(num)
sums=lambda arg1,arg2:arg1+arg2;
print("value:",sums(10,20))
print("value:",sums(10,20))
##########
sumss=lambda arg1:arg1*arg1*arg1;
print("cube",sumss(3))
tot=20#Global
def sums(arg1,arg2):
    tot=arg1+arg2#Local
    print(tot)
    return tot
sums(10,20)
print(tot)
##########
def cal(n):
    return n*n
numbers=(1,2,3,4)
result=map(cal,numbers)
print(tuple(result))
#########
num1=[4,5,6]
num2=[4,5,6]
res=map(lambda n1,n2:n1+n2,num1,num2)
print(list(res))
#filter
letters=['a','b','c','d','e','i','j','o']
def fil_vow(letter):
    vow=['a','e','i','o','u']
    if letter in vow:#passing name should be used as logical component inside function
        return True
    else:
        return False
fil=filter(fil_vow,letters)#same fucntion name also no problem
vowels=tuple(fil)
print(vowels)
#Filter Lambda
n=[1,2,3,4,5,6,7]
even_num=filter(lambda x:(x%2==0),n)
e=tuple(even_num)
print(e)
#########
from functools import reduce
def do_sum(x,y):
    return x+y
print(reduce(do_sum,[1,2,3,4]))
#######
def ch(val):
    if val.islower():
        return val.upper()
    elif val.isupper():
        return val.lower()
    else:
        return val
n=input("Enter a String")
for i in n:
    k=ch(n)
print(k)
###########
b=[]
def li(ele):
    k=ele**3
    return k
m=[1,2,3,4,5,6,7]
for i in m:
    b.append(li(i))
print(b)'''
#Exam
'''num = input("Enter a three-digit number: ")
num1={
    "0":"zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"four",
    "5":"Five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"Nine"
    }
num2={
    "0":"Ones",
    "1":"Tens",
    "2":"hunderes",
    "3":"thousand",
    "4":"ten thousand",
    "5":"Lakhs",
    "6":"Ten lakhs",
    "7":"crore"
    }
for i in range(len(num)):
    k=num[i]
    print(num1[k] + " " + num2[str(len(num)-i-1)], end=" ")
#conv
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
my_dict = dict(zip(keys, values))
print(my_dict)
#sum of dict
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
total_sum = 0
for value in my_dict.values():
    total_sum += value
print("Sum of all values:", total_sum)
#dicts mark
details = {
    "name1": "Alice",
    "mark1":45,
    "name2": "ice",
    "mark2":41,
    "name3": "Aliva",
    "mark3":43
}
print("Details before ")
print(details)
details.popitem()
details.popitem()
print("After Deletion")
print(details)
#large
def l(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(l(30,50,70))
#count
def count_characters(text):
    digit_count = 0
    uppercase_count = 0
    lowercase_count = 0
    for char in text:
        if char.isdigit():
            digit_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return digit_count, uppercase_count, lowercase_count
user_input = input("Enter a string: ")
#strings = ["Hello", "123", "World", "AbC"]
a,b,c = count_characters(user_input)
print(f"Number of digits: {a}")
print(f"Number of uppercase letters: {b}")
print(f"Number of lowercase letters: {c}")
#square
dict1 = {}
for num in range(1, 6):
    dict1[num] = num ** 2
print(dict1)
#odd
def filter_odd_numbers(input_list):
    odd_numbers = []
    for num in input_list:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers
numbers = [3, 8, 9, 7, 6, 5]
odd_numbers_list = filter_odd_numbers(numbers)
print("Odd numbers:", odd_numbers_list)
#print
print('He said, "What\'s there?"')
#radius
def area(radius):
    area = 3.14*radius ** 2
    return area
print(area(5))
#divible
def is_divisible_by_11(number):
    return number % 11 == 0
num = int(input("Enter an integer: "))
if is_divisible_by_11(num):
    print(f"{num} is divisible by 11.")
else:
    print(f"{num} is not divisible by 11.")
#Palindrome
def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original_number == reversed_number
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")'''
#
#
#*******************************************#
# 1. Find the maximum of three numbers
def find(num1, num2, num3):
    result = max(num1, num2, num3)
    print(result)
find(1,2,3)
# 2. Sum all the numbers in a list
def sums(numbers):
    result = sum(numbers)
    print(result)
list1=[]
for i in range (5):
    list1.append(int(input()))
sums(list1)
# 3. Multiply all the numbers in a list
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    print(result)
list1=[]
for i in range (5):
    list1.append(int(input()))
multiply(list1)
# 4. Reverse a string
def reverse(input_string):
    result = input_string[::-1]
    print(result)
reverse("Harish")
# 5. Count upper and lower case letters in a string
def count_upper_lower_case_letters(input_string):
    upper_count = 0
    lower_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
input_string = input("Enter a string: ")
upper_count, lower_count = count_upper_lower_case_letters(input_string)
print("Uppercase:", upper_count)
print("Lowercase:", lower_count)
# 6. Create a list of squares of numbers from 1 to 30
def create_squares_list():
    result = []
    for i in range(1, 31):
        result.append(i**2)
    print(result)
create_squares_list()
# 7. Find the largest item in a list
def find_largest_item(input_list):
    result = max(input_list)
    print(result)
list1=[]
for i in range (5):
    list1.append(int(input()))
find_largest_item(list1)
# 8. Function with a default argument
def greet(name="harish"):
    result = f"Hello, {name}!"
    print(result)

# 9. Example for *args
def example_args(*args):
    print(args)
example_args(1,2,3,4,4,5)
# 10. Convert lowercase words to uppercase
def convert_to_uppercase(input_string):
    result = input_string.upper()
    print(result)
convert_to_uppercase("harish")
# 11. Calculate the area of a circle
def calculate_circle_area(radius):
    result = 3.14159 * (radius ** 2)
    print(result)
calculate_circle_area(3)
# 12. Check if a number is divisible by 11
def is_divisible_by_11(number):
    result = number % 11 == 0
    print(result)
is_divisible_by_11(333)
# 13. Check if a number is palindrome
def is_palindrome(number):
    result = str(number) == str(number)[::-1]
    print(result)
is_palindrome(333)
