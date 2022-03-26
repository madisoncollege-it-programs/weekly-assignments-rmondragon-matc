#!/usr/bin/env python3 

def degrees_celsius():

    fahrenheit = int(input("What is the temperature in Fahrenheit?"))
    print(" The temperature in fahrenhheit is:  ",fahrenheit)
 
    celsius = (fahrenheit * 5/9 - 32)

    print("The temperature in celsius is: ", celsius)

degrees_celsius()
