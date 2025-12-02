class Car:
    brand = "Volvo"
    color = "White"
    
car1 = Car()
print (car1.brand)

car2 = Car()
print (car2.color)


class Vehicle:
    def __init__(self, brand, doors, wheels = 4 ):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels
        
    def car_greeting(self, local_slang):
        print(f"Your car brand is {self.brand} aka {local_slang}")
        

Veh1 = Vehicle("VW", 2)

veh2 = Vehicle("BMW", 2)