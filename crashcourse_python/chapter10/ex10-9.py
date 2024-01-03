# Exercise 10-9
# Similar to ex. 10-8, only that a file is ignored if it does not exist (no error message)

# filenames = ["catnames.txt", "dognames.txt"]

# file "canames.txt" is ignored
filenames = ["canames.txt", "dognames.txt"]

for filename in filenames:
    try:
        with open(filename, 'r') as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        print("\nContents of the file " + filename + ":")
        print(contents)