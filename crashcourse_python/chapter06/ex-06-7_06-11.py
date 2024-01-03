
# ex 6-7
# exercise for practicing nesting dictionaries in a list

person1 = {
    'first_name': "Maxine",
    'last_name': "Muster",
    'gender' : "female",
    'age': 20,
    'city': "Muenchen",
    'birthday': "01.02.2003"
    }

person2 = {
    'first_name': "Bob",
    'last_name': "Bobinsky",
    'gender' : "male",
    'age': 52,
    'city': "Moscow",
    'birthday': "15.11.1970"
    }

person3 = {
    'first_name': "Barbie",
    'last_name': "Roberts",
    'gender' : "female",
    'age': 64,
    'city': "New York City",
    'birthday': "09.03.1959"
    }

people = [person1, person2, person3,]

for person in people:
    if person['gender'] == "female":
        print(person['first_name'] + " " + person['last_name'] + " is " 
              + str(person['age']) + " years old. " + "She is from "
              + person['city'] + ". Her birthday is on " + person['birthday'] + "."
              )
    
    elif person['gender'] == "male":
        print(person['first_name'] + " " + person['last_name'] + " is " 
              + str(person['age']) + " years old. " + "He is from "
              + person['city'] + ". His birthday is on " + person['birthday'] + "."
              )
print()       
        
        
        
# ex 6-8
# exercise for nesting dictionaries in a list

pet1 = {
    'animal' : "cat",
    'owner' : "Barbie",
    'name' : "Bertie",
    'fav-food' : "salmon",
        }

pet2 = {
    'animal' : "mouse",
    'owner' : "Bobinsky",
    'name' : "Jerry",
    'fav-food' : "swiss cheese",
        }
        
pet3 = {
    'animal' : "snake",
    'owner' : "Maxine",
    'name' : "Othello",
    'fav-food' : "mice",
        }

pets = [pet1, pet2, pet3,]

for pet in pets:
    print(pet['owner'] + " owns a " + pet['animal'] + ". The " + pet['animal'] 
          + "'s name is " + pet['name'] + " and it likes to eat " + pet['fav-food'] 
          + ".")
print()       



# ex 6-9
# exercise for nesting lists in a dictionary

favorite_places = {
    'Mathilde' : ["Paris"],
    'Olaf' : ["bed", "kitchen refrigerator", "cinema"],
    'Bob' : ["Mallorca", "New York", "garden"],
    }

for name in favorite_places.keys():
    if len(favorite_places[name]) > 1:
        print("\n" + name + "'s favorite places are: " )
        for place in favorite_places[name]:
            print("\t" + place)
    else:
        print(name + "'s favorite place is: ")
        print("\t" + favorite_places[name][0])
print()        



# ex 6-11
# nesting dictionaries in a dictionary

cities = {
    'Manila' : {
        'country' : "the Philippines",
        'population' : 1846000,
        'area' : "42.34 km^2",
        'age' : "over 800",
        'fact' : "densest city in the world",
        },
    
    'Trier' : {
        'country' : "Germany",
        'population' : 110600,
        'area' : "117.1 km^2",
        'age' : "over 2000",
        'fact' : "oldest city in Germany",
        },
    
    'Chongqing' : {
        'country' : "China",
        'population' : 31020000,
        'area' : "82339 km^2",
        'age' : "3000",
        'fact' : "largest city by area",
        },
    }

for city, data in cities.items():
    print("\nThe city " + city + " is in " + data['country'] 
          + ". It has a population of " + str(data['population']) 
          + " and an area of " + data['area']
          + ". It is " + data['age'] + " years old. A fact about this city is that it is the "
          + data['fact'] + "."
          )
    










        
        
        
        