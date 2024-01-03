
# ex 8-9
# make a list and print each item in the list using a function
magicians = ["Harry Houdini", "David Copperfield", "Mickey Mouse"]

def show_magicians(m):
    print("\nA list of magicians:")
    for magician in m:
        print("\t" + magician)    

show_magicians(magicians)


# ex 8-10
# change the previous list using a function and print the list to show that the 
# list has indeed been changed

def make_great(m):
    for i in range(len(m)):
        m[i] = m[i] + " the Great"        

make_great(magicians)
show_magicians(magicians)
print()
print(magicians)
