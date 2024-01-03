# Exercises for the input() function
# input() is a function which stops the program and prompts the user to enter an 
# input. The  given input is stored in a string variable. input() takes one argument, 
# the prompt text (the text displayed when the user is prompted to give an input)
# Note: if the input is a number, it must be converted to a number data type first 
# (e.g. with int()) before calculations can be done on the input (since the input 
# is stored as a string by default)



# ex 7-1 using the input function

fav_flavor = input("Tell me your favorite flavor of ice cream: ")
print("One scoop of " + fav_flavor + " ice cream, coming up.\n")



# ex 7-2 

prompt = "How many guests are to be seated? Enter a number from 1-100: "
num_guests = int(input(prompt))
if 1 <= num_guests <= 8 :
    print("A table for " + str(num_guests) + " people is available. Please be seated.\n")
elif 8 < num_guests <= 100 :
    print("We currently have no tables for more than 8 people. Please wait to be seated. \n")



# ex 7-3 
prompt = "Please enter a number: "
num = input(prompt)
if int(num) % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("Your input " + num + " is not a multiple of 10.")
    
    

# Recall: For takes a collection of elements (e.g. a list) and carries out a 
# code block once for each element in the collection. 
# A while loop, is carried out as long as a certain condition is true
















