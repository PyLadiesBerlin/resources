print()
print("Welcome to the dungeon!")
print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print("Congratulations, you found a new friend!")
    elif vampire == "2":
        print("Sorry, the vampire is faster. You become a dinner.")
    else:
        print("You are not so good with numbers, are you?")

# GET CREATIVE:
# add door 2 here with elif.

else:
    print("You are not so good with numbers, are you?")
