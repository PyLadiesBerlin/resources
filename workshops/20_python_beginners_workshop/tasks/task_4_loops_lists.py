'''
TASK 04

Lets use loops and lists!!

A - Create a variable named `friends` and add a list of names that the users friends.
B. When a user enters some room, print that her friend X is in the room. To use a
name from the list, eg. friends[0], friends[1] can be used.
C. Make this name to be chosen randomly. Import Python library random, that has functions to help
with random numbers and use random.randint(a, b) function to give you a random number between a and b. eg.
random.randint(1,4) will give a random number among 1, 2, 3, 4
D - Extend your death function telling the user that is failing from high: Eg. print
"You are failing for..."
 1
 2
 3
 ...
 30
 ... meters! You are dead".
Try to print all the numbers up to 30 or 50 with a for loop using range function, eg. range(30) will return
some kind of list with numbers from 0-29
E - Add a delay between the failing with time.sleep(secs), Eg. time.sleep(1) will pause the program for 1 sec. Remember to add
import time in the beginning of the code.
'''
# Exercise C the import goes here

# Exercise A
# friends =

print()

print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    # Exercise B, C
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print("Congratulations %s, you found a new friend!" % (name))
    elif vampire == "2":
        print("Sorry %s, the vampire is faster. You become a dinner." % (name))
    else:
        # Your code from Task 3 should be here

# Your code from Task 1 should be here

else:
    wrong_input()

# Your code from Task 2 should be here

