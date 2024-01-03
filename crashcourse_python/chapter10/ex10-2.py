# exercise 10-2
# edit a text using the replace() method
# replace multiple strings using a dictionary and a loop

filename = "cats.txt"

char_to_replace = {
    "Cats " : "Dogs ",      # add space so words containing "cat-" (like catch) don't get edited
    "cats " : "dogs ",
    "Cat " : "Dog ",
    "cat " : "dog ",
    "cats." : "dogs.",
    "cat." : "dog."
    }

with open(filename) as file_obj:    # left out read/write argument in open(). -> default mode: read (r)
    message = file_obj.read()
    print("Original message:")
    print(message)
    print("\nNew message:")
    for key, value in char_to_replace.items():
        message = message.replace(key, value)
    print(message)
