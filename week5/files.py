#!/usr/bin/env python3

import sys

#Ryley Mondragon, The purpose of this exercise was to use different data types to read and display the contents


#1

hFile = open("/etc/passwd","r")
stringfiletext = hFile.readlines()
stringfiletext = str(stringfiletext)
print(stringfiletext)
print(type(stringfiletext))
print( len(stringfiletext))
hFile.close()

print( "The len() function counts the number of items in an object\n")
print( "Using the read function over the alternatives in this scenario is more useful because we are just opening and closing the file, no appending or saving.\n")

#2
hFile = open("/etc/passwd","r")
listfiletext = hFile.readlines()
print(listfiletext)
print(type(listfiletext))
print(len(listfiletext))
hFile.close

print( "The len() function counts the number of items in an object\n")
print( "Using the read function over the alternatives in this scenario is more of a benefit because if I wanted to use /n it would output as a new line instead of counting it as part of the function\n")

#3

hFile = open("/etc/passwd","r")
listfiletext = hFile.readlines()
listfiletext = str(listfiletext)
print(listfiletext)
print(type(listfiletext))

def count_words(listfiletext):
    listfiletext=listfiletext.strip()
    count=1
    for element in listfiletext:
        count+=1
    return count
print( count_words(listfiletext))

hFile.close

print( "Using a loop a read function is useful because it returns and stores each iteration of the loop")



