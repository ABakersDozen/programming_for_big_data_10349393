
from car import ElectricCar, PetrolCar, DieselCar, HybridCar

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
        self.rented_cars = []
    
    def create_current_stock(self):
        self.overallTotal = 40
        # Making an assumption here that the dealer will maintain the current 
        # ratio of 50% petrol, 20% diesel, 10% electric and 20% hybrid  
        for i in range(int(self.overallTotal*0.5)):
           self.petrol_cars.append(PetrolCar())
        for i in range(int(self.overallTotal*0.2)):
           self.diesel_cars.append(DieselCar())
        for i in range(int(self.overallTotal*0.2)):
           self.hybrid_cars.append(HybridCar())
        for i in range(int(self.overallTotal*0.1)):
           self.electric_cars.append(ElectricCar())

    def stock_count(self):
        print 'Petrol cars in stock {}\n'.format(len(self.petrol_cars))
        print 'Diesel cars in stock {}\n'.format(len(self.diesel_cars))
        print 'Petrol cars in stock {}\n'.format(len(self.hybrid_cars))
        print 'Electric cars in stock {}\n'.format(len(self.electric_cars))


    def rent(self, car_list, rented_cars, amount):     # Process to rent a car function        
        if len(car_list) < amount:
            print 'Not enough cars in stock.\n'     # Make sure enough cars in stock
            return
        total = 0
        while total < amount:
            carout = car_list.pop()          # Pop last item from given car list and return it
            self.rented_cars.append(carout)       # Then append to a new list of rented cars that are now unavailable
            total = total + 1
            print 'Make: ' + carout.getMake()       
            print 'Colour: ' + carout.getColour()
            print 'Engine Size(Cylinders): ' + carout.getEngineSize()            
        print 'You have rented ' + str(amount) + ' car(s)\n'       
        return rented_cars
    
    def rented(self, car_list, rented_cars, amount):  # Process for returning cars        
        total = 0
        while total < amount:
            carin = self.rented_cars.pop()
            car_list.append(carin)
            total = total + 1
        print 'You have returned' +str(amount) + 'car(s)\n'
        return rented_cars, car_list
    
    def rental_system(self): # returns and rental
        rentedcars = []
        rented = raw_input('Are you returning or renting a car? Type either RETURN or RENT\n')
        if rented.lower() == 'return':       # Return system
            type = raw_input('Are you returning a petrol, electric, diesel or hybrid car?\n')
            amount = raw_input('How many would you like to return?\n')
            if type == 'petrol':
                self.rented(self.petrol_cars, rentedcars, amount)
            elif type.lower() == 'diesel':
                self.rented(self.diesel_cars, rentedcars, amount)
            elif type.lower() == 'hybrid':
                self.rented(self.hybrid_cars, rentedcars, amount)
            elif type.lower() == 'electric':
                self.rented(self.electric_cars, rentedcars, amount)
            else:
                print 'Error, please check your spelling.\n'
                return
        elif rented.lower() == 'rent':        # Rental system
            answer = raw_input('What type of car would you like? Type: petrol/diesel/hybrid/electric\n')
            amount = int(raw_input('How many of that type of car?\n'))
            if answer.lower() == 'petrol':
                self.rent(self.petrol_cars, rentedcars, amount)
            elif answer.lower() == 'diesel':
                self.rent(self.diesel_cars, rentedcars, amount)
            elif answer.lower() == 'hybrid':
                self.rent(self.hybrid_cars, rentedcars, amount)
            elif answer.lower() == 'electric':
                self.rent(self.electric_cars, rentedcars, amount)
            else:
                print 'Error, please check your spelling.\n'
                return

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.rental_system()
    proceed = raw_input('Would you like to continue? Y/N\n')