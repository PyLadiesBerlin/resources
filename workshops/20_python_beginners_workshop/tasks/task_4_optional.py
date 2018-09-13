'''
TASK 04

A - Check if the input the user gave you is bigger/smaller than 50 with: if int(some_input) > 50
B - Create actions for each case (bigger or smaller)
'''

# Your code from Exercise A on Task 3 should be here

# Your code from Exercise C on Task 3 should be here

print()
# Your code from Exercise A on Task 2 should be here

# Your code from Exercise B on Task 2 should be here

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
        dead("Sorry %s, the vampire is faster. You become a dinner." % (name))
    else:
        # Your code from Exercise B on Task 3 should be here

# Your code from Task 1 should be here

else:
    wrong_input()

# Your code from Exercise C on Task 2 should be here

# Exercise A
    # Exercise B
