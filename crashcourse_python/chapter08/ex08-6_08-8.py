

# ex 8-6
# a function which returns something

def city_country(city, country):
    #string = city + ", " + country
    #return string.title()
    return city.title() + ", " + country.title()

x = city_country("berlin", "germany")
y = city_country("amsterdam", "netherlands")
# print(x)
# print(y)
# print()
    


# 8-7
# returning a dictionary from a function and having an optional key-value pair
def make_album(artist="N/A", title="N/A", number_tracks=""):
    album = { 
        'artist name' : artist, 
        'album title' : title
        }
    if number_tracks:  # assign number_tracks to key tracks if argument is not left empty
        album['tracks'] = int(number_tracks)
    return album

album1 = make_album("Alt-J", "An Awesome Wave")
album2 = make_album("Overwerk", "Canon")
album3 = make_album("Hot Sugar", "Moon Money", "9")
album4 = make_album(title="The Dark Side of the Moon")
# print(album1)
# print(album2)
# print(album3)
# print(album4)



# 8-8
# make a dictionary with user input 
def make_albums(artist="N/A", title="N/A"):
    album = { 
        'artist name' : artist, 
        'album title' : title
        }
    return album

while True:
    print("\nEnter an artist name and an album title. Enter q at any time to quit.")
    artist = input("\tArtist: ")
    if artist == "q":
        break
    title = input("\tTitle: ")
    if title == "q":
        album = make_albums(artist)
        print("\nCreated a dictionary for the album: ")
        print(album)
        break
    album = make_albums(artist, title)
    print("\nCreated a dictionary for the album: ")
    print(album)


