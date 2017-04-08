# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:19:06 2017

@author: 10349393
"""
# import required functions from the math library
from math import sin, cos, sqrt, radians, factorial

class Calculator:
    # basic unit initilisation
    def __init__(self):
        self.data = [] # not required but added in case something is required later
    
    # sum function, adds numbers together
    def sum(self, n1, n2):
        return n1 + n2
    
    # subtract function, takes one number from another
    def subtract(self, n1, n2):
        return n1 - n2
    
    # multiples two numbers
    def multiply(self, n1, n2):
        return n1 * n2
    
    # divides one number by another, watches for division by zero error
    def divide(self, n1, n2):
        if n2 == 0:
            return 'Cannot divide by zero'
        else:
            return n1 / float(n2) #only need one converted to float
    
    # returns one number to the power of a second
    def power(self, n1, n2):
        return n1 ** n2
    
    # this returns the square of one number
    def square(self, n1):
        return n1 * n1   
    
    # this returns the square root of a number, it watches for negative numbers and zero to prevent errors
    def squarert(self, n1):
        if n1 <= 0:
            return 'This program does not return a value for values < 0'
        else:
            return sqrt(n1)                
    
    # returns the sine of passed degrees. sine function by default using radians so the degrees are converted first
    # number of decimal places restricted for testing purposes
    def sin_degrees(self, n1):
        return sin(radians(n1)) 
    
    # returns the cosine of passed degrees. cosine function by default using radians so the degrees are converted first
    # number of decimal places restricted for testing purposes
    def cos_degrees(self, n1):
        return cos(radians(n1)) 
    
    # returns the factorial of a number, watches for negative numbers and zero to prevent errors
    def factorial_func(self, n1):
        if n1 <= 0:
            return "I'm afraid this program can't calculate that"
        else:
            return factorial(n1)

# this is the options screen presented on every iteration of the program
def options_screen():
    print '\n*********************\n'
    print "What calculation would you like to do:\n"
    print "1)Addition of two numbers\n2)Subtraction of two numbers\n3)Multiplication of two numbers"
    print "4)Division of two numbers\n5)One number to the power of a second\n6)Square a number"
    print "7)Square-root a number\n8)Factorial of a number\n9)Sine value of degrees"
    print "10)Cosine value of degrees\n"
    print "Please enter a selection to proceed. (Q to exit.)"
    print '\n*********************\n'
    str_input = raw_input("> ")
    return str2int(str_input) # calls another function to check the input
    
# this function will check if the value entered can be converted from a string to an integer
def str2int(user_input):
    if user_input.lower() == 'q':
        return 999 # this will exit the loop
    try:
        choice = int(user_input)
        if choice < 1 or choice > 10 : return None # this out of 'scope' check could be more descriptive using the error code it returns
        else : return choice
    except:
        return None

# this function will check if the value entered can be converted from a string to a float
def str2float(user_input):
    if user_input.lower() == 'q':
        return 'leave' # this will exit the loop, 999 isn't a safe error code return for amount!
    try:
        number = float(user_input)
        return number
    except:
        return None


#opening text
if __name__ == '__main__':
    print "\n"
    print "Welcome! This is a simple calculator tool.\n"
    
    rain_man = Calculator()
    
    #starts a loop to keep the program running as long as the user wants
    while True:
    # this loads the options function so the user has a choice
        choice = options_screen()
        if choice == 999: # quit has been selected in the options function
            print "\n\n\n\nGoodbye.\n" # a sad goodbye message
            break # breaks the loop and exits
        elif choice == None: # error handling from the functions - we could use variations of this this for unique error codes
            print "\n"
            print "You didn't make a valid selection, try again or Q to quit.\n"
            raw_input("Hit any key to continue.\n") # this is so the user can read the text before the next text prints
            continue
        else: # errors and exit handled, we move on to the calculator
            print "\n"
            if choice <= 5:
                str_input = raw_input("What is the first number you want to use for that operation?\n\n> ")
                number1 = str2float(str_input)
                if number1 == 'leave': # quit has been selected
                    print "\n\n\n\nGoodbye.\n" # a sad goodbye message
                    break
                elif number1 == None: # error handling from the functions - we could use this for unique error codes
                    print "\n"
                    print "You didn't make a valid entry, try again or Q to quit.\n"
                    raw_input("Hit any key to continue.")
                    continue
                else:
                    str_input = raw_input("What is the second number you want to use for that operation?\n\n> ")
                    number2 = str2float(str_input)
                    if number2 == 'leave': # quit has been selected
                        print "\n\n\n\nGoodbye.\n" # a sad goodbye message
                        break
                    elif number2 == None: # error handling from the functions - we could use this for unique error codes
                        print "\n"
                        print "You didn't make a valid entry, try again or Q to quit.\n"
                        raw_input("Hit any key to continue.")
                        continue
                    else: # errors and exit handled, we can convert the user's input now
                        if choice == 1:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.sum(number1, number2))
                        elif choice == 2:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.subtract(number1, number2))
                        elif choice == 3:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.multiply(number1, number2))
                        elif choice == 4:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.divide(number1, number2))
                        elif choice == 5:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.power(number1, number2))
            elif choice > 5 and choice < 9:
                str_input = raw_input("What number do you want to use for that operation?\n\n> ")
                number1 = str2float(str_input)
                if number1 == 'leave': # quit has been selected
                    print "\n\n\n\nGoodbye.\n" # a sad goodbye message
                    break
                elif number1 == None: # error handling from the functions - we could use this for unique error codes
                    print "\n"
                    print "You didn't make a valid entry, try again or Q to quit.\n"
                    raw_input("Hit any key to continue.")
                    continue
                else:
                        if choice == 6:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.square(number1))
                        elif choice == 7:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.squarert(number1))
                        elif choice == 8:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.factorial_func(number1))
            elif choice == 9 or choice == 10:   
                str_input = raw_input("Please enter the number of degrees you wish to convert?\n\n> ")
                number1 = str2float(str_input)
                if number1 == 'leave': # quit has been selected
                    print "\n\n\n\nGoodbye.\n" # a sad goodbye message
                    break
                elif number1 == None: # error handling from the functions - we could use this for unique error codes
                    print "\n"
                    print "You didn't make a valid entry, try again or Q to quit.\n"
                    raw_input("Hit any key to continue.")
                    continue
                else:
                        if choice == 9:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.sin_degrees(number1))
                        elif choice == 10:                  
                            # we now print the user's new calculated value to screen
                            print "\nThe result of that operation is: {}".format(rain_man.cos_degrees(number1))
                            
                            
                            
            #we give the user a chance to exit or loop again
            str_input = raw_input("Would you like to return to the main menu or quit?\nAny key to continue, Q to quit.\n> ")
            if str_input.lower() == 'q':
                print "\n\n\n\nGoodbye.\n" # a sad goodbye message
                break
            else:
                print "\n" * 20 # Makes the next menu more obvious by spacing it out. Using a system call we could alternatively clear the screen.
                continue