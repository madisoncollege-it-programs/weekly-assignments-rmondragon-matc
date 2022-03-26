#!/usr/bin/env python3

def degrees_fahrenheit():

    celsius = int(input(" What is the temperature in celsius?"))
    print(" The temperature in celsius is: ",celsius)

    fahrenheit = (celsius * 9/5 + 32)

    print("The temperature in fahrenheit is: ",fahrenheit)

degrees_fahrenheit()
