# Exercise 10-8
# open and read each file in a list;
# if a file does not exist print error and continue to execute the code on
# the existing file

# files in the list must exist in the same directory where the program is saved
filenames = ["catnames.txt", "dognames.txt"]

# Nonexistent file leads to error for that filename while the code still works 
# for the existing file
# filenames = ["canames.txt", "dognames.txt"]

for filename in filenames:
    try:
        with open(filename, 'r') as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print("\nThe file " + filename + " does not exist in the current directory!")
    else:
        print("\nContents of the file " + filename + ":")
        print(contents)