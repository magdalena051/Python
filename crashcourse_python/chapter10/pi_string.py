filename = "pi_digits.txt" 

with open(filename) as file_object:
    lines = file_object.readlines() # readlines() stores each line of the text file 
                                    # in a list (each line is an element of the list)
                                    # lines is a list
                                 
# we can continue to work with the list lines after the file is closed
pi_string = ""
for line in lines:
    pi_string += line.strip()        # there are extra spaces on the left and
                                     # after each line there is an extra whitespace row, 
                                     # so use strip() to remove the whitespace
    
print(pi_string)
print(len(pi_string))