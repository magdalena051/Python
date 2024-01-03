# count how often a word appears in a text

filenames = ["frankenstein.txt", "frankenstein_words.txt", "greatgatsby.txt"]

words = ["frankenstein", " the", "blue", "green"]

for filename in filenames:
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print("The file " + filename + " does not exist!")
    else:
        print("\nAnalysing " + filename + ":")
        for word in words:
            count = contents.lower().count(word)
            print("\tThe word \"" + word + "\" appears in this file " + str(count) + " times.")
            
            
