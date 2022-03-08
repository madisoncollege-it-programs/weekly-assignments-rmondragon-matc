#!/usr/bin/env python3


print("Name: Ryley Mondragon")

#This acitvity is to go through Flow Control for the Midterm.

Total = 0

keywords = "gmeach18@ed.gov","248.253.63.149","Whiteland","80.222.19.190","Kayley","dcassyqw@microsoft,com"

with open("Midterm-if.txt", "r") as hFile:
    for line in hFile:
        if "Whiteland" in line:
            print(f" {line} ") 
            Total += 11 
        elif "gmeach18@ed.gov" in line:
            print(f" {line} ")
            Total += 45
        elif "248.253.63.149" in line:
             print(f" {line} ")
             Total += 345
        elif "80.222.19.190" in line:
             print(f" {line} ")
             Total += 525
        elif "Kayley" in line:
             print(f" {line} ")
             Total += 530
        elif "dcassyqw@microsoft.com" in line:
             print(f" {line} ")
             Total += 969
        
            
print(f"The Total is: {Total}")




