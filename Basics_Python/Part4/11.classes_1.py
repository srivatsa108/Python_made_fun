#classes is a group of functions
class vehicle(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def brake(self):
        return "The vehicle is braking"
    def drive(self):
        return "The vehicle is driving"
    

#subclass 
class vehiclesub(vehicle):
    def brake(self):
        return "this is a subclass of vehicle"
    
    if __name__ == "__main__":
        print("within the main function")
        
#main code
car=vehiclesub("Car", 200, 20)
print(car.brake())
print(car.drive())
        