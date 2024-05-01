#Speed
'''a=int(input("Enter distance :"))
b=int(input("Enter Time :"))
c=a/b
print("The Speed of a bus:",c)'''
#Typeconv
'''a = input("Enter an integer: ")
b= input("Enter a string: ")
c = input("Enter a float: ")
int_a = int(a)
str_b = str(b)
float_c = float(c)
print("Converted int variable:", int_a)
print("Converted str variable:", str_b)
print("Converted float variable:", float_c)'''
#pyramid
'''n=int(input("Enter a number"))
for i in range(1,n+1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()'''
#Factorial
'''for i in range(1, 11):
    result = 1
    for j in range(1, i + 1):
        result *= j
    print(f"Factorial of {i} is: {result}")'''
#Cube
'''limit = int(input("Enter the limit: "))
cubes = 0
for num in range(1, limit + 1):
    cubes += num ** 3
print("Sum of cubes of numbers up to the limit:", sum_cubes)'''
#Factor
'''number = int(input("Enter a two-digit number: "))
print("Factors of", number, "are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)'''
#R Traingle
'''n=int(input("Enter a number"))
for i in range(1,n+1):
    for j in range(i):
         print("*",end="")
    print()'''
#+ Pattern
'''n=int(input("Enter the number:"))
for i in range(n):
    for j in range (n):
            if(n%2!=0):  
                if i==n//2 or j==n//2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            else:
                if i==n//2-1 or j==n//2-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")         
    print()'''
#Arrow Mark
n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==n//2 or i+j==n+n//2-1 or j-i==n//2:
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print()

