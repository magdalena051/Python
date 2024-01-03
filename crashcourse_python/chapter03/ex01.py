# Page 43
bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles[0])
# print(bicycles[-4])
# print(bicycles[0].title())


# page 44
# exercise 3-1
names = ["Anna", "Bob", "Claudia", "Doris"]
for i in range(len(names)):  # default starting value for range(a,b) is a=0
    print(names[i])
print("\n")

# exercise 3-2
for i in range(len(names)):
    print("Hello, " + names[i])
print("\n")    
    

# page 46
# insert, delete, pop functions
# del vs. pop: if want to continue using the deleted element, use pop,
#              otherwise use del
names.insert(1, "Billy")
print(names)

del names[1]
print(names)

popped_name = names.pop()
print(names)
print(popped_name)

