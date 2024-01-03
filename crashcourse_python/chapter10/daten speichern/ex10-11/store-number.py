# Section saving and reading user generated data
# ex 10-11

import json 

filename = "fav_number.json"

def get_valid_input():
    flag = True
    while flag == True:
        fav_number = input("What is your favorite number? Enter an integer number: ")
        if fav_number.isnumeric():
            flag = False
            return fav_number
        else:
            print("Please enter a valid input!")

fav_number = get_valid_input()

with open(filename, "w") as file_obj:
    json.dump(fav_number, file_obj)
    