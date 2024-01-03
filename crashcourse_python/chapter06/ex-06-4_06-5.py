###########################################################################
# testing out key / value properties. Dictionary keys are like strings, the 
# values can be any data type

favorite_numbers = {
    'Anna': 8,
    'Bob': 127,
    'Charlie': 13,
    'Donnie': 3.14159,
    'Emma' : 5
    }

names = ""
for name in favorite_numbers.keys():
    names = names + name + " "
print("Keys in the dictionary:  " + names)

sum = 0
for num in favorite_numbers.values():
    sum = sum + num
print("Sum of the numbers in the dictionary:  " + str(sum))
#print(" ")
#
############################################################################


# Exercises to practice accessing keys, values, keys and values of a dictionary, 
# and using for to loop through the dictionary key/value enries

# ex 6-4

python_dict = {
    'variable': "Ein symbolischer Name welcher ein Objekt referenziert",
    'string': "Ein Datentyp, der eine Folge von Zeichen darstellt",
    'liste': "Eine geordnete Sammlung von Elementen, umschlossen mit '[ ]'",
    'dictionary': "Datentyp bestehend aus einer Sammlung von Schlüssel-Wert Paaren",
    'if-Anweisung' : "Kontrollstruktur welche eine Bedingung als true oder false auswertet",
    'for-Schleife' : "Nimmt eine Zusammenstellung von Elementen entgegen und führt einen Codeblock für jedes der darin enthaltenen Elemente aus"
    }

print("\nBegriff    " + "  | Definition")
for key, val in python_dict.items():
    padkey = " "                       # for formatting
    while len(key) <= 11:              #
        key = key + padkey             #
    print(key.title() + " | " + val)
print()


# ex 6-5

rivers = {
    'nile' : 'egypt',
    'elbe' : 'germany',
    'mississippi': 'united states',
    'amazon' : 'brazil',
    'yangtze' : 'china',
    'yenisey' : 'russia'
    }

for river, country in rivers.items():
    print("The " + river.title() + " river runs through " + country.title() + ".")
print()

rivernames = ""
for river in rivers.keys():
    rivernames = rivernames + river.title() + ", "
print("River names contained in the dictionary: " + rivernames)
    
countrynames = ""
for country in rivers.values():
    countrynames = countrynames + country.title() + ", "
print("Country names contained in the dictionary: " + countrynames)
print()

# ex 6-6

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    'leon' : 'rust',
    'bob' : 'scratch',
    }

names = ['jen', 'sarah', 'edward', 'phil', 'leon', 'bob', 'marcel', 'lena', 'sally',]

for name in sorted(names):
    if name in favorite_languages.keys():
        print(name.title() + "'s favorite language is " + favorite_languages[name].title() 
              + ". Thanks for taking the poll, " + name.title() + "!")
    else:
        print(name.title() + ", please take the poll!")



