
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
        uniqueID = 100
        # Making an assumption here that the dealer will maintain the current 
        # ratio of 50% petrol, 20% diesel, 10% electric and 20% hybrid  
        for i in range(int(self.overallTotal*0.5)):
           self.petrol_cars.append(PetrolCar(uniqueID))
           uniqueID += 1
        for i in range(int(self.overallTotal*0.2)):
           self.diesel_cars.append(DieselCar(uniqueID))
           uniqueID += 1
        for i in range(int(self.overallTotal*0.2)):
           self.hybrid_cars.append(HybridCar(uniqueID))
           uniqueID += 1
        for i in range(int(self.overallTotal*0.1)):
           self.electric_cars.append(ElectricCar(uniqueID))
           uniqueID += 1

    def stock_count(self):
        print "\nPetrol cars in stock {}".format(len(self.petrol_cars))
        print "Diesel cars in stock {}".format(len(self.diesel_cars))
        print "Petrol cars in stock {}".format(len(self.hybrid_cars))
        print "Electric cars in stock {}\n".format(len(self.electric_cars))

    def rent(self, car_list, amount, customerID):     # Process to rent a car function        
        if len(car_list) < amount:
            print "Not enough cars in stock.\n"     # Make sure enough cars in stock
            return
        total = 0
        while total < amount:
            carout = car_list.pop()          # Pop last item from given car list and return it
            self.rented_cars.append([carout, customerID])       # Then append to a new list of rented cars that are now unavailable
            total += 1
            print "\nRental Car Unique ID: {}".format(carout.getID())
            print "Make: {}".format(carout.getMake())      
            print "Colour: {}".format(carout.getColour())
            print "Engine Size(Litres or Battery Size): {}".format(carout.getEngineSize())            
        print "\nYou have rented {} car(s)\n".format(amount) 
    
    def rented(self, customerID):  # Process for returning cars        
        amount = 0
        i=0
        proceed = "y"
        while proceed.lower() == "y":  
            while i<len(self.rented_cars):
                if self.rented_cars[i][1] == customerID:
                    print "Rental {}:".format(i+1)
                    print "Rental Car Unique ID: {}".format(self.rented_cars[i][0].getID())
                    print "Type: {}".format(self.rented_cars[i][0].getType()) 
                    print "Make: {}".format(self.rented_cars[i][0].getMake()) 
                    print "Colour: {}\n".format(self.rented_cars[i][0].getColour())
                    i += 1
                else:
                    i += 1
                    continue
            returns = raw_input("Please enter the Rental Car Unique ID you would like to return:\n") 
            i=0
            while i<len(self.rented_cars):
                if self.rented_cars[i][0].getID() == int(returns):
                    listout = self.rented_cars.pop(i)
                    carin = listout[0]
                    if carin.getType() == "Petrol":
                        self.petrol_cars.append(carin)
                    elif carin.getType() == "Diesel":
                        self.diesel_cars.append(carin)
                    elif carin.getType() == "Hybrid":
                        self.hybrid_cars.append(carin)
                    elif carin.getType() == "Electric":
                        self.electric_cars.append(carin)
                    break
                else:
                    i += 1
                    continue
            amount +=1
            proceed = raw_input("Would you like to return another car? (Y/N)\n")    
        print "You have returned {} car(s)\n".format(amount) 
    
    def nested(self, customerID):
        return any(customerID in nested for nested in self.rented_cars)
               
    def rental_system(self): # returns and rental
        customerID = raw_input("\nWhat is the unique customer ID?\n")
        rented = raw_input("Do you wish to rent out or return a car? Type either (1)Rent or (2)Return\n")
        
        if rented.lower() == "rent" or rented.lower() == "1":        # Rental system
            self.stock_count()
            Sorry nothing to rent, please try again
            answer = raw_input("What type of car would you like? Type: \n(P)etrol\n(D)iesel\n(H)ybrid\n(E)lectric\n")
            amount = int(raw_input("How many of that type of car?\n"))
            if answer.lower() == "petrol" or answer.lower() == "p":
                self.rent(self.petrol_cars, amount, customerID)
            elif answer.lower() == "diesel" or answer.lower() == "d":
                self.rent(self.diesel_cars, amount, customerID)
            elif answer.lower() == "hybrid" or answer.lower() == "h":
                self.rent(self.hybrid_cars, amount, customerID)
            elif answer.lower() == "electric" or answer.lower() == "e":
                self.rent(self.electric_cars, amount, customerID)
            else:
                print "Error, please check your spelling.\n"
                return
        elif rented.lower() == "return" or rented.lower() == "2":       # Return system
            if not self.rented_cars:
                print "Error, there are no rentals to return!\n"
                return
            elif self.nested(customerID) == False:  
                print "Error, please check the customer ID entered, there are no rentals under that ID.\n"
                return 
            else:
                self.rented(customerID)
        else:
            print "Please make a valid selection.\n"
            return

    def getRentedTotal(self):
        i=0
        while i<len(self.rented_cars):
            print "Rental Car Unique ID: {}".format(self.rented_cars[i][0].getID())
            print "Customer ID rented to: {}\n".format(self.rented_cars[i][1])
            i += 1

# enable so that this is only called when the script run from the command line
if __name__ == '__main__':
    dealership = Dealership()
    dealership.create_current_stock()
    proceed = "y"
    while proceed.lower() == "y":
        dealership.rental_system()
        proceed = raw_input("Would you like to continue? (Y/N)\n")
    dealership.stock_count()
    dealership.getRentedTotal()