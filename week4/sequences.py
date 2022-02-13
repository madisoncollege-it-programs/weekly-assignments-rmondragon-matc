#!/usr/bin/env python3

import sys

#Ryley Mondragon, This script contains my exercise for Data Types.

varString = "Here is a nice string to slice"
varList = ["Here","is","a","nice","list","to","slice"]

#2

print(f" {varString[3:32]}")

print(f" {varString[0:3]}")

print(f" {varString[3:12]}")

print(f" {varString[0:4:2]} {varString[6:11]} {varString[12]} {varString[14:21:2]} {varString[22]} {varString[26:29:2]}")

print(f" {varString[::-1]}")

#3

print(f" {varList[::-1]}")

print(f" {varList[2::-1]}")

print(f" {varList[2:4:1]}")

print(f" {varList[0:7:3]}")

print(f" {varList[1::1]}")

#4

for element in varString: print(element)

for element in varList: print(element)



