# Topic: writing to files
# exercise 10-3
# ask for user's name and save name in a text file

filename = "guest.txt"

name = input("Hello, guest. What is your name? ")

with open(filename, 'a') as file_obj:
    file_obj.write(name + "\n")
