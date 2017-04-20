# Define a class for the car

# ****** Note I could have created lists for colour, car make/model, engine/battery size 
# and then use the random funtion to uniquely vary each car instance as it is created. I opted not to build this functionality in but it is possible.

class Car(object):
    # implement the car object, every car is considered brand new.    
    def __init__(self):
        self.colour = "Aungier Rental Red - Branded" # we'll brand all cars the same colour here
        self.mileage = 0 # off the manufacturing line...

    # return the instance colour
    def getColour(self):
        return self.colour
    
    # return the instance unique ID
    def getID(self):
        return self.uniqueID

    # return the instance car type
    def getType(self):
        return self.type
    
    # return the instance car make
    def getMake(self):
        return self.make
    
    # return the instance milage
    def getMileage(self):
        return self.mileage
    
    # return the instance engine/battery size
    def getEngineSize(self):
        if self.engineSize is None:
            return self.batterySize
        else:
            return self.engineSize

 # below functions not used in the Dealership program but included for completeness   
    # change the instance make   
    def setMake(self, make):
        self.make = make
     
    # change the instance model       
    def setModel(self, model):
        self.make = model

    # change the instance milage   
    def setMileage(self, mileage):
        self.mileage = mileage

    # change the instance colour   
    def paint(self, colour):
        self.colour = colour

    # add any new milage to the car   
    def move(self, distance):
        self.mileage = self.mileage + distance
        return self.mileage

# the classes for each car 'type' are outlined below, all values defaulted but as stated above a random list could have been used in each case to create variety
# a unique ID is passed from the calling (e.g.: Dealership) class as each instance is created. 
class ElectricCar(Car):
    def __init__(self, uniqueID):
        Car.__init__(self)
        self.make = 'Tesla'
        self.model = 'Model S P85D' 
        self.engineSize = None
        self.batterySize = '85-kWh'
        self.uniqueID = uniqueID
        self.type = 'Electric'
    
class PetrolCar(Car):
    def __init__(self, uniqueID):
        Car.__init__(self)
        self.make = 'Toyota'
        self.model = 'Avensis' 
        self.engineSize = '1.6 ltr'
        self.uniqueID = uniqueID
        self.type = 'Petrol'
        

class DieselCar(Car):
    def __init__(self, uniqueID):
        Car.__init__(self)
        self.make = 'Volkswagon'
        self.model = 'Passat' 
        self.engineSize = '1.9 ltr'  
        self.uniqueID = uniqueID
        self.type = 'Diesel'
    
    
class HybridCar(Car):
     def __init__(self, uniqueID):
        Car.__init__(self)
        self.make = 'Mitsubishi'
        self.model = 'Outlander PHEV' 
        self.engineSize = '2.0 ltr'
        self.uniqueID = uniqueID
        self.type = 'Hybrid'