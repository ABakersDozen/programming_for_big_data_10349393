# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:19:06 2017

@author: 10349393
"""
# for use in our test cases we import the calculator 'library'
from calculator import Calculator
# import the testing feature
import unittest

                  
class MyTest(unittest.TestCase):
    def setUp(self):
        self.robot = Calculator()
        
    # a function to test the addition feature   
    def testAdd(self):
        self.assertEqual(self.robot.sum(2,2), 4)
        self.assertEqual(self.robot.sum(5,3), 8)
        self.assertEqual(self.robot.sum(5,0), 5)
        self.assertEqual(self.robot.sum(3,4), 7)

    # a function to test the subtraction feature     
    def testSubtract(self):
        self.assertEqual(self.robot.subtract(2,2), 0)
        self.assertEqual(self.robot.subtract(5,3), 2)
        self.assertEqual(self.robot.subtract(5,0), 5)
        self.assertEqual(self.robot.subtract(3,4), -1)

    # a function to test the multiplication feature     
    def testMultiply(self):
        self.assertEqual(self.robot.multiply(2,2), 4)
        self.assertEqual(self.robot.multiply(5,3), 15)
        self.assertEqual(self.robot.multiply(5,0), 0)
        self.assertEqual(self.robot.multiply(3,4), 12)

    # a function to test the division feature     
    def testDivide(self):
        self.assertEqual(self.robot.divide(2,2), 1)
        self.assertEqual(self.robot.divide(5,4), 1.25)
        self.assertEqual(self.robot.divide(5,0), 'Cannot divide by zero')
        self.assertEqual(self.robot.divide(3,4), 0.75)

    # a function to test the 'to the power of' feature     
    def testPower(self):
        self.assertEqual(self.robot.power(2,2), 4)
        self.assertEqual(self.robot.power(5,4), 625)
        self.assertEqual(self.robot.power(5,0), 1)
        self.assertEqual(self.robot.power(3,4), 81)

    # a function to test the squaring feature     
    def testSquare(self):
        self.assertEqual(self.robot.square(2), 4)
        self.assertEqual(self.robot.square(5), 25)
        self.assertEqual(self.robot.square(1), 1)
        self.assertEqual(self.robot.square(10), 100)

    # a function to test the square root feature         
    def testSquareRt(self):
        self.assertEqual(self.robot.squarert(4), 2)
        self.assertEqual(self.robot.squarert(25), 5)
        self.assertEqual(self.robot.squarert(1), 1)
        self.assertEqual(self.robot.squarert(-100), 'This program does not return a value for values < 0')
                 
        # a function to test the sine of degrees feature  
    def test_sin_degrees(self):
        self.assertEqual(round(self.robot.sin_degrees(45), 11), 0.70710678119)
        self.assertEqual(round(self.robot.sin_degrees(30), 11), 0.5)
        self.assertEqual(round(self.robot.sin_degrees(90), 11), 1)
        self.assertEqual(round(self.robot.sin_degrees(-15), 11), -0.2588190451)
        
        # a function to test the cosine of degrees feature
    def test_cos_degrees(self):
        self.assertEqual(round(self.robot.cos_degrees(45), 11), 0.70710678119)
        self.assertEqual(round(self.robot.cos_degrees(30), 11), 0.86602540378)
        self.assertEqual(round(self.robot.cos_degrees(90), 11), 0)
        self.assertEqual(round(self.robot.cos_degrees(-15), 11), 0.96592582629)      

    # a function to test the factorial feature
    def test_factorial_func(self):
        self.assertEqual(self.robot.factorial_func(2), 2)
        self.assertEqual(self.robot.factorial_func(5), 120)
        self.assertEqual(self.robot.factorial_func(10), 3628800)
        self.assertEqual(self.robot.factorial_func(0), "I'm afraid this program can't calculate that")    


if __name__ == '__main__':
    unittest.main()
    