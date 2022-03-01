#!/usr/bin/env python3
import sys

script_name = sys.argv[0]
number_of_input_items = len(sys.argv)
input_list = str(sys.argv)
first_name = sys.argv[1]
last_name = sys.argv[2]

print(f"This is the name of my script: {script_name}")
print(f"Number of arguments          : {number_of_input_items}")
print(f"The arguments are            : {input_list}")
print(f"Argument 1                   : {first_name}")
print(f"Argument 2                   : {last_name}")

print(f" Your first name is {first_name}, Your last name is {last_name}")

print("I learned that Variables are different in Linux and Windows as compared to Python")
