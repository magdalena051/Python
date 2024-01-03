# page 50-51, exercises 

# ex. 3-4
guests = ["Alice", "Barry", "Carmen", "Dorian", "Edmund"]
for i in range(len(guests)):
    print("Hello " + guests[i] + ", you are invited to dinner")
print("\n")
    

# ex. 3-4
canceled_guest = guests[4]
print(canceled_guest + " can't come to dinner.")
print("\n")

new_guest = "Edward"
guests[4] = new_guest
for i in range(len(guests)):
    print("Hello " + guests[i] + ", you are invited to dinner")
print("\n")


# ex. 3-6
print("Good news people, I have found a bigger table.")
print("\n")
guests.insert(0, "Antonia")
guests.insert(2, "Charlie")
guests.append("Ella")
for i in range(len(guests)):
    print("Hello " + guests[i] + ", you are invited to dinner")
print("\n")


# ex. 3-7
print("Bad news people, I can only invite two of you.")
while len(guests)>2:
    guest = guests.pop()
    print("I'm sorry " + guest + ", you can't come after all.")
print(guests)
for i in range(len(guests)):
    print("Hello " + guests[i] + ", you are still invited to dinner.")
del guests[1]
del guests[0]
print(guests)



