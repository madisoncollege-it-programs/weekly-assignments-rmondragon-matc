#!/usr/bin/env python3


#Ryley Mondragon, the purpose of this script is to call other scripts that run a conversion function


measure = input(" What is the measurement?")

if measure == "celsius":

    import c2f
#imports the celsius to fahrenheit conversion file
elif measure == "fahrenheit":

    import f2c

#import the fahrenheit to celsius conversion file

