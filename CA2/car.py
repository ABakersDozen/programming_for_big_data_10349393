# Define a class for my car

class Car(object):
    # implement the car object.    
    def __init__(self):
        self.colour = "Aungier Rental Red - Branded"
        self.mileage = 0
        self.rentalStatus = 0 # 0 indicates not rented, 1 will indicate not available

    def getColour(self):
        return self.colour
    
    def getID(self):
        return self.uniqueID

    def getMake(self):
        return self.make
    
    def getStatus(self):
        return self.rentalStatus

    def getMileage(self):
        return self.mileage
    
    def getEngineSize(self):
        if self.engineSize is None:
            return self.batterySize
        else:
            return self.engineSize

    def setMake(self, make):
        self.make = make
        
    def setModel(self, model):
        self.make = model

    def setMileage(self, mileage):
        self.mileage = mileage

    def paint(self, colour):
        self.colour = colour

    def move(self, distance):
        self.mileage = self.mileage + distance
        return self.mileage


class ElectricCar(Car):
    def __init__(self, uniqueID):
        Car.__init__(self)
        self.make = 'Tesla'
        self.model = 'Model S P85D' 
        self.engineSize = None
        self.batterySize = '85-kWh'
        self.uniqueID = uniqueID
    
class PetrolCar(Car):
    def __init__(self, uniqueID):
        Car.__init__(self)
        self.make = 'Toyota'
        self.model = 'Avensis' 
        self.engineSize = '1.6 ltr'
        self.uniqueID = uniqueID
        

class DieselCar(Car):
    def __init__(self, uniqueID):
        Car.__init__(self)
        self.make = 'Volkswagon'
        self.model = 'Passat' 
        self.engineSize = '1.9 ltr'  
        self.uniqueID = uniqueID
    
    
class HybridCar(Car):
     def __init__(self, uniqueID):
        Car.__init__(self)
        self.make = 'Mitsubishi'
        self.model = 'Outlander PHEV' 
        self.engineSize = '2.0 ltr'
        self.uniqueID = uniqueID