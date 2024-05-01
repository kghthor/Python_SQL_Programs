h={"Harish","Geetha","Kumar"}
b={"Harishk","kilo","bilo","dilo"}
'''print(h)
print(type(h))
print(len(h))
set2={1,5,7,9,3}
set3={True,False,False,0,1}
print(set3)
for i in b:
    print(b)
print("Harish" in b)
b.add("Whoose")
print(b)
#print(h.update(b))
z=["Harish","kilo","bilo","dilo"]
h.update(z)
print(h)
#z.remove("Kiwi")
#print(z)
#z.discard("kiwi")
#print(z)
#del z
#print(z)
b.intersection_update(h)
print(b)
h.intersection_update(b)
print(h)'''
if(h.isdisjoint(b)):
    print("no common")
else:
    print("common")
    print(h.intersection(b))
