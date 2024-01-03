# Section saving and reading user generated data

# greet a user whose name was stored in the previous program (remember_me.py)


import json

filename = "username.json"

with open(filename, 'r') as file_obj:
    username = json.load(file_obj)              # the json file contains only a single name (one string)
    print("Welcome back, " + username + "!")
