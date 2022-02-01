#!/usr/bin/env python3

import sys

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

#Q1
print(f"Hello {varName}")
#Q2
print(f"{varRed}-{varGreen}-{varBlue}")
#Q3
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")
#Q4
print(f"My name is {varName.upper()}")
#Q5
print(f"[{varRed:+^7s}]")
#Q6
print(f"[{varGreen:=<7s}]")
#Q7
print(f"[{varBlue:*>9s}]")
#Q8
print(f"{varBlue*9}")
#Q9
print(f"{varLoot}")
#Q10
print(f"{varLoot:<.1f}")
#Q11
print(f"I have ${varLoot:<.4}")
#Q12
print(f"[{varRed:$^10s}][{varGreen:$^10s}][{varBlue:$^10s}]")
#Q14
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
