print()
print("What is your name?")

# store input in 'name' 
name = input("> ")

# use input in a print statement
print("Hello %s, welcome the the dungeon!" % (name))
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

# GET CREATIVE:
# Ask your player a second question and use the answer.

else:
    print("You are not so good with numbers, are you?")
