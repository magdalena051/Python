# Topic: writing to files
# ex 10-5
# Ask user for response and add each response to a text file, until user quits


filename = "survey_results.txt"

flag = True

print("Welcome to my survey about programming. Enter 'q' at any time to quit.")

while flag == True:
    response = input("Why do you like programming? Give a few words saying why. ")
    if response == "q":
        print("Thank you for taking part in the survey!")
        flag = False
    else:
        with open(filename, 'a') as file_obj:     # 'a' is append mode
            file_obj.write(response + "\n")
    