# ex 09-7
# write a subclass Admin that inherits from User and additionally has an attribute
# privileges and a method which displays the privileges 

class User():
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        
    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name + "'s user details: \
              \n\tUsername: " + self.username + "\n\tAge: " + str(self.age))
            
    def greet_user(self):
        print("\nHello " + self.first_name + " " + self.last_name + "! "  
              + self.username + " is a nice username.")



class Admin(User):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("User " + self.username + " is an admin. They have the following privileges:")
        for privilege in self.privileges:
            print("\t" + privilege)        
        

admin1 = Admin("Ada", "Lovelace", "addie")
admin1.show_privileges()