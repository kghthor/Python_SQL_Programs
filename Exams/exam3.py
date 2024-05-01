try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    my_list = [1, 2, 3]
    index = 5
    value = my_list[index]
    print(value)
except IndexError:
    print("Error: Index is out of range.")

try:
    w= open("nonexistent_file.txt")
    content = w.read()
    print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")

a = 5
b = "zero"

try:
    quotient = a / b
    print(quotient)
except ZeroDivisionError:
    print("You cannot divide by zero")
except TypeError:
    print("You must convert strings to floats or integers before dividing")
except NameError:
    print("A variable you're trying to use does not exist")
#add content,read, append ,count
fil=open("text.txt","w")
fil.write("Sharing makes our life happy baa, baa\n")
fil.write("The more we share the more we have baa, baa\n")
fil.write("Sharing makes our life joyful baa, baa\n")
fil.write("Sharing is a way of caring baa, baa\n")
fil.close()
d=open("text.txt")
c = d.read()
print(c)
d.close()
d=open("text.txt")
print(d.read(9))
fi= open("text.txt", "a")
fi.write("Jack and Jill went up the hill\n")
fi.write("To fetch a pail of water;\n")
fi.close()
op=open("text.txt")
k=op.read()
print(k)
words = k.split()
word_count = len(words)
print("Word count in the poem:", word_count)
#create file
'''ab= open("new_file.txt", "x")
ab.write("This is a new file created using 'x' mode.")'''


