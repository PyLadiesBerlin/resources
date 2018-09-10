'''
TASK 02
Now that you created new doors for your player to choose from, let's personalize the game a little bit. Write the answer to each exercise under its related inline comment.
A - Ask the name of the player and store the answer on a variable.
B - Use the variable in which you stored the players name to print a welcoming.
C - Time to get creative! Ask one more question to the player and use their answer.
'''

print()
# Exercise A

# Exercise B

print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
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
        print("You are not so good with numbers, are you?")

# Your code from Task 1 should be here

else:
    print("You are not so good with numbers, are you?")

# Exercise C
