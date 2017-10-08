print()
print("What is your name?")

name = input("> ")

print("Hello %s, welcome the the dungeon!" % (name))
print("Do you go through door 1 or door 2?")

# create function
def wrong_input():
    print("You are not so good with numbers, are you?")

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
        # use function
        wrong_input()

# GET CREATIVE:
# how would you write a dead-function using an argument called death_message?

else:
    wrong_input()