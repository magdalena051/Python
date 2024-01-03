filename = "pi_million_digits.txt" 

with open(filename) as file_object:
    lines = file_object.readlines() 
                                 
pi_string = ""
for line in lines:
    pi_string += line.strip()

n = 52 
n = n-2
print("First " + str(n) + " decimals of pi: " + pi_string[:52] + "...")

print("\nTotal length of the stored pi string: " + str(len(pi_string)))

birthday = "51097"
#birthday = "311091"

if birthday in pi_string:
    print("\nYour birthday is contained in the first 1 million digits of pi!")
    position = pi_string.find(birthday)-1
    print("\nThe first occurence is the " + str(position) + "-th decimal of pi.")
else:
    print("\nYour birthday is not contained in the first 1 million digits of pi!")