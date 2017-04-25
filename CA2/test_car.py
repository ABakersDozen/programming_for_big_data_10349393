import unittest

from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar # import the different types of 'Car' class
from Aungier_Car_Rental import Dealership

"""
red_car = Car()
print 'Colour ' + red_car.getColour()

red_car.paint('red')
print 'Colour ' + red_car.getColour()


print 'Engine Size ' + red_car.engineSize
red_car.engineSize = '3.9'
print 'Engine Size ' + red_car.engineSize
"""

# test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car1 = ElectricCar(1)
        self.car2 = PetrolCar(2)
        self.car3 = DieselCar(3)
        self.car4 = HybridCar(4)
        self.dealership = Dealership()
        self.dealership.create_current_stock()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15) # this function exists for all child classes of car
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.car.setMake('Ferrari') # this function exists for all child classes of car
        self.assertEqual('Ferrari', self.car.getMake())
        self.assertEqual('Ferrari', self.car.getMake())
        self.assertEqual('Tesla', self.car1.getMake())
        self.assertEqual('Toyota', self.car2.getMake())
        self.assertEqual('Volkswagon', self.car3.getMake())
        self.assertEqual('Mitsubishi', self.car4.getMake())

    def test_car_colour(self):
        self.assertEqual("Aungier Rental Red - Branded", self.car.getColour())
        self.car.paint('red') # this function exists for all child classes of car
        self.assertEqual('red', self.car.getColour())
        
    def test_car_engine(self):
        self.assertEqual('85-kWh', self.car1.getEngineSize())
        self.assertEqual('1.6 ltr', self.car2.getEngineSize())
        self.assertEqual('1.9 ltr', self.car3.getEngineSize())
        self.assertEqual('2.0 ltr', self.car4.getEngineSize())

    def test_rentalprocess(self): # test the rental process by renting out one car and checking it back in. verifies stock levels also
        self.assertEqual(0, len(self.dealership.rented_cars))
        self.assertEqual(8, len(self.dealership.hybrid_cars))
        self.dealership.rent(self.dealership.hybrid_cars,1,"Test")
        self.assertEqual(1, len(self.dealership.rented_cars))
        self.assertEqual("Test",self.dealership.rented_cars[0][1])
        self.assertEqual(7, len(self.dealership.hybrid_cars))
   
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: "135"
        self.assertEqual(self.dealership.rented("Test"),None)
        __builtins__.raw_input = original_raw_input
        
        self.assertEqual(0, len(self.dealership.rented_cars))
        self.assertEqual(8, len(self.dealership.hybrid_cars))
        

if __name__ == '__main__':
    unittest.main()
