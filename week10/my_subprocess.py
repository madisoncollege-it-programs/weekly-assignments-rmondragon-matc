#!/usr/bin/env python3
import subprocess


myProc = subprocess.run((["ps","-axco","command"]), stdout=subprocess.PIPE)
myProcString = myProc.stdout.decode().split('\n')

#runs the subprocess off of the import that then decodes and splits the text line by line

for element in myProcString:
    print(element)

print(len(myProcString))

#Cuts out the first element and counts the number of lines that will print at the end of the command.
