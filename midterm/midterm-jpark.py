#!/usr/bin/env python3


print("Ryley Mondragon")

#This script is  to initialize object with flow control and dictionaries for the Midterm"

password_database = {"Username":"dnedry","Password":"please"}

command_database = {"a. reboot":"OK. I will reboot all park systems.","b. shutdown":"OK. I will shut down all park systems.","c. done":"I hate all this hacker stuff"}

white_rabbit_object = 0

counter = 0

while (white_rabbit_object == 0 and counter < 3):
    input_user = input("Enter Username: ")
    input_password = input("Enter Password: ")
    if (input_user == "dendry") and \
        (input_password == "please"):
            white_rabbit_object = 1
            print("Hi, Dennis You're still the best hacker in Jurassic Park.")
            print(f"{command_database.keys()}:  ")
            input_command = input("Enter a command:")
            if (input_command == "reboot"):
                print("OK. I will reboot all park systems.")
            elif (input_command == "shutdown"):
                print("OK. I will shut down all park systems.")
            elif (input_command == "done"):
                print("I hate all this hacker stuff")
            elif (input != "reboot","done","shutdown"):
                print("The Lysine Contigency has been put into effect") 
    elif (input_user != password_database['Username']) and \
        (input_password != password_database['Password']):
            counter += 1
            print(f"You did not say the magic word. {counter}")
            if counter == 3: 
                print("You did not say the magic word\n" * 25)
 

