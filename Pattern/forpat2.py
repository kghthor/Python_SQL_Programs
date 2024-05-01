'''n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()
A 
B B 
C C C 
D D D D 
E E E E E'''
    
'''n=int(input("Enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
A 
A B 
A B C 
A B C D 
A B C D E'''

'''n=int(input("Enter a number"))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(64+i),end=" ")
    print()
A A A A A 
B B B B 
C C C 
D D 
E'''

'''n=int(input("Enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c5hr(79+j),end=" ")
    print()
P 
P Q 
P Q R 
P Q R S 
P Q R S T '''

'''
P 
Q Q 
R R R 
S S S S 
T T T T T '''
#small variation in last print kinda off  pyramid shape but not correct, change i give number pyramid or j column impacted
#Alphabetic Pyrammid
n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(n-i):
         print(" ",end=" ")
    for k in range(2*i-1):
        print(chr(64+i),end=" ")
    print()
#Reverse the Pyramid
'''n=int(input("Enter a number"))
for i in range(n,0,-1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()'''
#Reverse the  Alphabetic Pyramid
'''n=int(input("Enter a number"))
for i in range(n,0,-1):
    for j in range(n-i):
         print(" ",end="")
    for k in range(2*i-1):
        print(chr(64+i),end="")
    print()'''
#Arrow mark Problem pattern
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==n//2 or i+j==n+n//2-1 or j-i==n//2:
            print("*",end=" ")
        else:
            print(' ',end=' ')
    print() '''

