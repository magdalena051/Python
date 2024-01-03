# for ex 9-11
# save User, Privileges and Admin here as a module to be imported 
# and used in a separate file

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


class Privileges():
    def __init__(self):
        self.privileges = []
        
    def add_privileges(self, new_privilege):
        self.privileges.extend(new_privilege)     
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges()