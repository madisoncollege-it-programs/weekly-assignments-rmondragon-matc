#!/usr/bin/env python3


#Ryley Mondragon, this script is to show examples of decision logic.



print("""You enter a dark room with three doors.
Do you go through door #1 or door #2 or door #3?""")

door = input("-> ")

# == Door Number 1 logic ==============
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ====================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("bear runs away.")

# == Door Number 2 Logic ===============
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")

    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

 
# == Insanity Logic ====================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":

        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print("N)The insanity rots your eyes into a pool of muck. ")
        print("N) Good job!")

# == Door Number 3 logic ===============
elif door == "3":
     print("You stare into an endless blizzard.")
     print("What is your next move?.\n")


     print("1. Curl into a ball and cry.")
     print("2. Start walking.")
     print("3. Try to find a Dairy Queen.") 

# == Blizzard logic ============
     blizzard = input("-> ")

     if blizzard == "1":

         print("1)Your get picked up by a Yeti mother.")
         print("1)You made a new home in your forever environment!")
     elif blizzard == "2":
         print("2)You go crazy and freeze to death. ")
         print("2) Good job!")
     elif blizzard == "3":
        print("3)You found a Dairy Queen and you got free ice cream.")
        print("3)You never got out, but hey free ice cream.")


else:
    print("You did not select a door??? Good Call :)")

