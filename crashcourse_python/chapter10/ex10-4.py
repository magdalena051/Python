# exercise 10-4
# ask user for names and add them each to a file, with one line for each name 

filename = "guestbook.txt"

flag = True

while flag == True:
    name = input("What is your name? Press q to quit. ")
    if name == "q":
        flag = False
    else:
        print("\tHello, " + name + "! Adding you to the guestbook.")
        with open(filename, 'a') as file_obj:   # 'a' is append mode
            file_obj.write(name + "\n")
            