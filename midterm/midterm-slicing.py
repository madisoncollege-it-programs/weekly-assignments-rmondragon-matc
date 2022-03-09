#!/usr/bin/env python3


print("Ryley Mondragon")

#This activity is Splicing  for the midterm

hFile = open("slicing-file.txt","r") 
slicingfiletext = hFile.readlines()
#4.A
print(f" {slicingfiletext[24:25]}")
#4.B
print(f" {slicingfiletext[2:5]}")
#4.C
print(f" {slicingfiletext[-10]} {slicingfiletext[-12]} {slicingfiletext[-14]}")
#4.D
print(f" {slicingfiletext[10:13]}")
#4.E
print(f" {slicingfiletext[-19:1:-22]}  {slicingfiletext[-20]} {slicingfiletext[-21]}")


slicingA = ["Whether"]
slicingB = ["You", "Think", "you"]
slicingC = ["live","or","can"]
slicingD = ["think","you","cant"]
slicingE = ["class","taken","run"]
quote = "Whether you think you can or you think you cant, you are right"


print(f" {slicingfiletext[24:25]} {slicingfiletext[2:5]} {slicingfiletext[-10]} {slicingfiletext[-12]} {slicingfiletext[-14]} {slicingfiletext[10:13]} {slicingfiletext[-19:1:-22]}  {slicingfiletext[-20]} {slicingfiletext[-21]}")


