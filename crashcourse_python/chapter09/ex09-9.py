# ex 9-9
# add a new method upgrade_battery to the battery class.
# Create an instance of electric_car with the default battery size, then show 
# the range, upgrade the battery, and show the (upgraded) range again

class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()



class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + self.battery_size + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range) + \
            " miles on a full charge."
        print(message)
        
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print("This car's battery has been upgraded to a " + str(self.battery_size) \
                  + "-kWh battery.")    
    
    

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
        
my_ecar = ElectricCar("Tesla", "Model 3", "2022")
print(my_ecar.get_descriptive_name())
my_ecar.battery.get_range()
my_ecar.battery.upgrade_battery()
my_ecar.battery.get_range()
