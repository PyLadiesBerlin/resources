'''
TASK 05

Dictionaries!

Dictionaries are super useful python data structures and if you are dealing with data, like
wikipedia data, questionaire data, or anything you can imagine, dictionaries will prove useful.

A. Let's use a dictionary to describe each room. Create a dictionary variable called door_greetings
with keys the door numbers and values the door greeting. eg. door_greetings = {'1': "Welcome to the paradise"}
B. When the user enters each room print the corresponding door greeting from the dictionary.
'''

# Exercise A
# door_greetings =

print()

print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    # Exercise B - print room greeting
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

