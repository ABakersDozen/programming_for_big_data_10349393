
from car import ElectricCar, PetrolCar, DieselCar, HybridCar # import the different types of 'Car' class. 

class Dealership(object): # this creates the dealership class

    def __init__(self): 
        # create list instances for each type pf car to rent out
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
        self.rented_cars = [] # this list will store the cars as they are rented out (so we can return them afterwards!)
    
    def create_current_stock(self):
        self.overallTotal = 40 # total stock the dealer plans on having initially
        uniqueID = 100 # each car will have it's own unique ID, this is the starting integer
        # Making an assumption here that the dealer will maintain the current 
        # ratio of 50% petrol, 20% diesel, 10% electric and 20% hybrid 
        # this could be changed to fixed qtys of each
        # 'build' the fleet!
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

    def stock_count(self): # a function to print to screen the current stock levels of each type of car
        print "\nPetrol cars in stock {}".format(len(self.petrol_cars))
        print "Diesel cars in stock {}".format(len(self.diesel_cars))
        print "Hybrid cars in stock {}".format(len(self.hybrid_cars))
        print "Electric cars in stock {}\n".format(len(self.electric_cars))

    def rent(self, car_list, amount, customerID):     # Process to rent a car function        
        if len(car_list) < amount: # Make sure there are enough cars in stock
            print "Not enough cars in stock.\n"     
            return
        total = 0
        while total < amount:
            carout = car_list.pop()          # Pop last item from reqested car type list and return it
            self.rented_cars.append([carout, customerID])       # Then append it to a the list of rented cars that are now unavailable
            total += 1
            # output to screen what has been rented
            print "\nRental Car Unique ID: {}".format(carout.getID())
            print "Make: {}".format(carout.getMake())      
            print "Colour: {}".format(carout.getColour())
            print "Engine Size(Litres or Battery Size): {}".format(carout.getEngineSize())            
        print "\nYou have rented {} car(s)\n".format(amount) 
    
    def rented(self, customerID):  # Process for returning cars        
        amount = 0 # 
        i=0
        proceed = "y"
        # output to screen what the customer currently has rented and then allow them to select the car(s) they would like to return until finished
        while proceed.lower() == "y":  
            while i<len(self.rented_cars):
                # only output what this unique customer has rented already
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
            # check all the rented cars in the list to find the one the cusomter wishes to return
            # add it back into the available pool of cars to rent of that type
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
            # chance to end the loop and exit
            proceed = raw_input("Would you like to return another car? (Y/N)\n")    
        # remind the cusomter how many cars they returned
        print "You have returned {} car(s)\n".format(amount) 
    
    def nested(self, customerID): # this function will check through the list of rented cars to see if a unique customer ID is present in the nested entries
        return any(customerID in nested for nested in self.rented_cars)
               
    def rental_system(self): # this function directs us to returns and rental functions as required
        customerID = raw_input("\nWhat is the customer ID you wish to use?\n")
        rented = raw_input("Do you wish to rent out or return a car? Type either (1)Rent or (2)Return\n")
        
        if rented.lower() == "rent" or rented.lower() == "1":        # Rental system
            self.stock_count()
            if len(self.rented_cars) >= self.overallTotal-1: # check there is any cars in stock first!
                print("Sorry nothing to rent, please try again.\n")
                return
            answer = raw_input("What type of car would you like? Type: \n(P)etrol\n(D)iesel\n(H)ybrid\n(E)lectric\n")
            # depending on user input makes sure we use the correct car type when checking out
            
            # ***** we could also pass the number of days they want to rent the car here. This could also be passed to the rental function and saved in the rental list. 
            
            if answer.lower() == "petrol" or answer.lower() == "p":
                amount = int(raw_input("How many of that type of car?\n"))
                self.rent(self.petrol_cars, amount, customerID)
            elif answer.lower() == "diesel" or answer.lower() == "d":
                amount = int(raw_input("How many of that type of car?\n"))
                self.rent(self.diesel_cars, amount, customerID)
            elif answer.lower() == "hybrid" or answer.lower() == "h":
                amount = int(raw_input("How many of that type of car?\n"))
                self.rent(self.hybrid_cars, amount, customerID)
            elif answer.lower() == "electric" or answer.lower() == "e":
                amount = int(raw_input("How many of that type of car?\n"))
                self.rent(self.electric_cars, amount, customerID)
            else:
                print "Error, please check your input.\n" # no valid selection or entry made
                return
        elif rented.lower() == "return" or rented.lower() == "2":       # Returns system
            # first check is there anything rented out in the first place!
            if not self.rented_cars:
                print "Error, there are no rentals to return!\n"
                return
            # next check has the current customer any rentals outstanding using the nested function above 
            elif self.nested(customerID) == False:  
                print "Error, please check the customer ID entered, there are no rentals under that ID.\n"
                return 
            else:
                self.rented(customerID)
        else:
            print "Please make a valid selection.\n"
            return

    def getRentedTotal(self): # this outputs the stock currentlyrented and the unique customer ID it is rented to.
        i=0
        while i<len(self.rented_cars):
            print "Rental Car Unique ID: {}".format(self.rented_cars[i][0].getID())
            print "Customer ID rented to: {}\n".format(self.rented_cars[i][1])
            i += 1

# enable so that this is only called when the script run from the command line
if __name__ == '__main__':
    dealership = Dealership() # initialise the class
    dealership.create_current_stock() # build intial stock
    proceed = "y"
    while proceed.lower() == "y":
        dealership.rental_system() # enter the rentals systems
        proceed = raw_input("Would you like to continue? (Y/N)\n")
    
    # on exiting output the remaining stock and then what/who the rented stock is registered to
    dealership.stock_count()
    dealership.getRentedTotal()