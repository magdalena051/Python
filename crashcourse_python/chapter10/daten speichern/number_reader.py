# using the function json.load
# json.load() reads data into working memory
# in this program, read the data that was stored in program number_writer.py
# using json.load() and output it

import json

filename = "numbers.json"               # make sure to choose the correct file
                                        # (here: the file we wrote to in the previous program)

with open(filename, 'r') as file_obj:   # open the file in read mode
    numbers = json.load(file_obj)       # json.load() takes a file object as parameter
                                        # and returns a json object

print(numbers)