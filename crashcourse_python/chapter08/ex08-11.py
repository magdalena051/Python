# ex 8-9
# make a list and print each item in the list using a function
magicians = ["Harry Houdini", "David Copperfield", "Mickey Mouse"]

def show_magicians(m):
    print("\nA list of magicians:")
    for magician in m:
        print("\t" + magician)    



# ex 8-11
# change a copy of the previous list using a function and return the changed copy
# print the original list and the copy to show that the original list is unchanged
# and the only the copy is changed

def make_great(m):
    for i in range(len(m)):
        m[i] = m[i] + " the Great"
    return m        

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
