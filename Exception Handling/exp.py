try:
    a=10
    b=0
    c=a/b
    print(c)#if two eception are there in a code it stops at one!
except ZeroDivisionError:
    print("Error")
except IndexError:
    print("IO error")
finally:
    print("king")
#***********************#
try:
    n=int(input())
    assert n%2==0
except:
    print("NOT even num")
else:
    r=1/n
    print(r)