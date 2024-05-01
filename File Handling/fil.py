'''file1= open("my.txt")#default by read
red=file1.read()
print(red)
file1.close'''
'''f=open("my.txt",'r')
print(f.readline())
for i in f:
    print(i)
f.close'''
f=open("new_file.txt", "a")
f.write("You are my fire")
f.close()
f=open("new_file.txt")
r=f.read()
print(r)
'''
f=open("abc.txt",'x')
f.write("thid ")
f.close'''