#Pascal Left Traingle
'''n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()'''
#Pascal Right Traingle
'''n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
         print("*",end="")
    print()'''
#General Alphabetic Pattern
'''n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(i):
        print(chr(64+i),end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(i):
        print(chr(64+i),end="")
    print()'''
#W Pattern
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or (i+j==n-1 and i>=n//2) or (i-j==0 and i>=n//2)):
             print("*",end="")
        else:
            print(" ",end='')
    print()'''
#   A Pattern
'''n=int(input("Enter number:"))
for i in range(n):
    for j in range(n):
            if i==0 or j==0 or j==n-1 or i==n//2 :
                print("*", end="")
            else:
                print(" ", end="")
    print()'''

#B code
'''n=int(input("Enter number:"))
for i in range(n):
    for j in range(n):
            if j == 0 or ((i == 0 or i == n//2 or i == n-1) and j < n-1) or (j == n-1 and i != 0 and i != n//2 and i != n-1):
                print("*", end="")
            else:
                print(" ", end="")
    print()'''

#C Code
'''n=int(input("Enter number:"))
for i in range(n):
    for j in range(n):
            if (i == 0 or i == n-1) and j > 0 or j == 0 and i > 0 and i < n-1:
                print("*", end="")
            else:
                print(" ", end="")
    print()
#D Code
n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
            if (i == 0 or i == n-1) and j < n-1 or j == 0 or j == n-1 and i > 0 and i < n-1:
                print("*", end="")
            else:
                print(" ", end="")
    print()
#E Code
n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
            if i == 0 or i == n-1 or j == 0 or (i == n//2 and j < n-1):
                print("*", end="")
            else:
                print(" ", end="")
    print()
#F code
n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
            if i == 0 or j == 0 or (i == n//2 and j < n-1):
                print("*", end="")
            else:
                print(" ", end="")
    print()'''
#Dimond
'''n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
         print("5 ",end="")
    for k in range(2*i-1):
        print(7"*",end="")
    print()'''
#Time Clock
'''n=int(input("Enter a number"))
for i in range(n,0,-1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*5",end="")
    print()
for i in range(1,n+1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()'''
#Pyramid Outline
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(2*n-1):
            if i + j == n-1 or j - i == n-1 or i == n-1:
                print("*", end="")
            else:
                print(" ", end="")
    print()'''
#Shape
'''n=int(input("Enter the number:"))
for i in range(n):
    for j in range (n):
                    if (i+j)%2==1:
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
    print()'''
#H Code
'''n=int(input("Enter the number:"))  
for i in range(n):
    for j in range(n):
            if j == 0 or j == n-1 or i == n//2:
                print("*", end="")
            else:
                print(" ", end="")
    print()'''
#I Code
'''n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j == n // 2 or i == 0 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#J Code
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if (i == 0 or j == n//2) or (i == n-1 and j < n//2) or (j == 0 and i > n//2):
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
#K code
'''n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or (i + j == n-1  and j>=n//2)  or (i == n // 2 and j==n//2) or i - j == 0 and j>=n//2:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
#L Code
'''n = int(input("Enter the number: "))

for i in range(n):
    for j in range(n):
        if j == 0 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#M Code
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(2 * n - 1):
        if j == 0 or j == 2 * n - 2 or i == j or i + j == 2 * n - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#N Code
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#O Code
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''    
#P Code
'''n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == n // 2  or (j==n - 1 and i<=n//2):
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
#Q Code
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 :
            print("*", end="")
        elif i == n // 2 + 1 and j == n - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#R Code
'''n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == n // 2 and j<=n//2 and j < n - 1 or (i + j == n-1  and j>=n//2) or i - j == 0 and j>=n//2 :
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
    
#S Code
'''n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n - 1 or i == n // 2) and j > 0 or (j == 0 and i < n // 2) or (j == n - 1 and i > n // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#T Code
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == n // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#U Code
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
#V Code
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(2 * n - 1):
        if i == j or i + j == 2 * n - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#X Code
'''n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
#Y Code
'''n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if j == n // 2 or (i + j == n-1  and j>n//2) or  i - j == 0 and j<n//2:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
#Z Code
'''n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

    










        
