# Chapter ten, section "Daten Speichern"
# JSON is a file format for saving and transmitting data
# JSON stands for JavaScript Object Notation
#
# json.dump()
# simple program using the function json.dump() to save data to a .json file 


import json

numbers = [2, 3, 5, 7, 11, 13, 17]

filename = "numbers.json"                   # data shall be stored in json format so we use 
                                            # .json file ending
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)               # json.dump() takes two parameters:
                                            # the data to be stored (here numbers)
                                            # and the file object for the file in which 
                                            # the data is to be stored
                                    


#############################################################################
# recall: if a file which is to be written to does not exist, open() together 
# with write parameter 'w' creates the file automatically (see page 221).
# But warning: if the file already exists, python empties the file before 
# returning the file object
                                    
filename2 = "test.txt"                      # this file initially does not exist

with open(filename2, 'w') as f_obj:         # open( , 'w') creates the file 
    f_obj.write("this is another test")