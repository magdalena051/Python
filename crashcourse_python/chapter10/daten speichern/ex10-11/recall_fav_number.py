
import json

filename = "fav_number.json"

with open(filename, "r") as file_obj:
    fav_number = json.load(file_obj)
    print("I know your favorite number! It's " + fav_number + ".")
