
from car import Car

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

    
def create_current_stock(self):
        overallTotal = 40
        '50% petrol, 20% diesel, 10% electric and 20% hybrid
        
        for i in range(20):
           self.electric_cars.append(Car(electric))
        for i in range(10):
           self.petrol_cars.append(PetrolCar())

    def stock_count(self):
        print 'petrol cars in stock ' + str(len(self.petrol_cars))
        print 'electric cars in stock ' + str(len(self.electric_cars))

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

petrol, diesel, electric, or hybrid cars.
They have initially 40 cars in their rental pool made up of 50% petrol, 20% diesel, 10% electric and 20% hybrid.