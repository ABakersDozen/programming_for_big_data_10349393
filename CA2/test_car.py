import unittest

from car import Car

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

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())

if __name__ == '__main__':
    unittest.main()
