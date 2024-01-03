
prompt = "I am a parrot. Tell me something, and I'll repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message + "\n")
print("You have entered 'quit'. The program is ending.")
