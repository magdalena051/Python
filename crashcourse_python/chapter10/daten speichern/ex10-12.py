# Section storing and reading user generated data
#
# Ask the user for their favorite number and store it to a json file. 
# If they have already been asked (if the file with their favorite number
# already exists), display the number. 

import json

filename = "fav_number.json"

try:
    with open(filename, "r") as file_obj:
        fav_number = json.load(file_obj)
    
except FileNotFoundError:
    # assume the user enters correct input
    fav_number = input("Enter your favorite number: ")
    with open(filename, "w") as file_obj:
        json.dump(fav_number, file_obj)
        print("Saved your favorite number. We'll remember it next time!")

else:
    print("I know your favorite number! It's " + fav_number + ".")