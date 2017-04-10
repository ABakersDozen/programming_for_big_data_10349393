
from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

    
    def create_current_stock(self):
        self.overallTotal = 40
        # Making an assumption here that the dealer will maintain the current 
        # ratio of 50% petrol, 20% diesel, 10% electric and 20% hybrid
        
        for i in range(int(self.overallTotal*0.1)):
           self.electric_cars.append(ElectricCar())
        for i in range(int(self.overallTotal*0.5)):
           self.petrol_cars.append(PetrolCar())
        for i in range(int(self.overallTotal*0.2)):
           self.diesel_cars.append(DieselCar())
        for i in range(int(self.overallTotal*0.2)):
           self.hybrid_cars.append(HybridCar())

    def stock_count(self):
        print 'Petrol cars in stock ' + str(len(self.petrol_cars))
        print 'Electric cars in stock ' + str(len(self.electric_cars))

    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print 'Not enough cars in stock'
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1

    def process_rental(self):
        answer = raw_input('would you like to rent a car? y/n')
        if answer == 'y':
            answer = raw_input('what type would you like? p/d')
            amount = int(raw_input('how many would you like?'))
            if answer == 'p':
                self.rent(self.petrol_cars, amount)
            else:
                self.rent(self.electric_cars, amount)
        self.stock_count()

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue? y/n')