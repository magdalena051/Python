# ex 9-5
# changing a class attribute via incrementing it via a method
# and resetting it via a method

class User():
    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = 0
        
    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name + "'s user details: \
              \n\tUsername: " + self.username + "\n\tAge: " + str(self.age))
            
    def greet_user(self):
        print("\nHello " + self.first_name + " " + self.last_name + "! "  
              + self.username + " is a nice username.")
    
    def get_login_attempts(self):
        print("Number of attempted logins: " + str(self.login_attempts))
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        

user = User("Maxi", "Muster", "acceptable_ad", 25)
user.get_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.reset_login_attempts()
user.get_login_attempts()