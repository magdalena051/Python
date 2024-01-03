# exercise 10-1
# print the contents of a file in three different ways

filename = "lines.txt"

with open(filename) as file_obj:
    # read and print the entire contents 
    contents = file_obj.read()
    print(contents)
print()   

with open(filename) as file_obj:
    # read and print the contents line by line
    for line in file_obj:
        print(line.rstrip())
print()           

with open(filename) as file_obj:
    # place the lines of the file in a list (each line is one list element)
    # and print the elements of the list
    lines = file_obj.readlines()
for line in lines:
    print(line.rstrip())