# ex 8-14

def make_car(brand, model, **extra_info):
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key, value in extra_info.items():
        car[key] = value
    return car
    
a_car = make_car("Volkswagen", "up", color="green", electric=True)
print(a_car)