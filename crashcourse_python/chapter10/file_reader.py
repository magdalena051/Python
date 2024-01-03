

# Use with keyword when opening and working with files -> no need to worry about
# closing the file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
    
## Cannot operate on file outside of with keyword; file is closed outside of with.
## So the following code leads to error "I/O operation on closed file" :
# contents2 = file_object.read() 


## Alternatively:
## instead of with keyword, open and explicitly close the file.
## Open file, store the file object in variable called file_object,
## read the file and store the text contents in a variable called contents,
## print the text contents,
## then close the file 
# file_object = open('pi_digits.txt')
# contents = file_object.read()
# print(contents)
# file_object.close()

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())    # rstrip() removes the extra whitespace on the right side
        
