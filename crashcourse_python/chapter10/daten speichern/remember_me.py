# Section: Saving and reading user generated data
# ask user for their name and store the name to a json file 

import json

username = input("What is your name? ")

filename = "username.json"

with open(filename, 'w') as file_obj:
    json.dump(username, file_obj)
    print("Saved your name to a json file. We'll remember you when you come back, "
          + username + "!")
    