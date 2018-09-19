'''
TASK 03

Functions time!

A - Create a function that prints and alert of wrong input (something to
substitute the answer of the else).
B - Use your function where it applies.
C - Now think a bit, how would you write a dead-function using an argument
called death_message? Create this function.
'''

# Exercise A

# Exercise C

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
        print("Sorry %s, the vampire is faster. You become a dinner." % (name))
    else:
        # Exercise B

# Your code from Task 1 should be here

else:
    wrong_input()

# Your code from Exercise C on Task 2 should be here

