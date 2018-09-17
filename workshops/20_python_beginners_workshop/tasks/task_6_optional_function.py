"""
TASK 06

Practice more functions. Use the code below.
A. Get creative write a function your_room. Check where it is called in the room
"""
from sys import exit

# start room
def start():

    choice = input("There is a door to your right and left. Which one do you take? ")

    if choice == "left":
        bank_room()
    elif choice == "right":
        your_room()
    else:
        dead("You stumble around the room until you starve.")

# second room
def bank_room():

    choice = input("This room is full of money. How many bank note bundles do you take? ")

    if choice.isdigit():

        if int(choice) > 0 and int(choice) < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        elif int(choice) > 50:
            dead("You greedy bastard!")

    else:
        dead("Man, learn to type a number.")


# Exercise A

def dead(why):
    print(why, "You are dead.")
    exit(0)

start()
