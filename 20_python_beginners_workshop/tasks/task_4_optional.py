print()
print("What is your name?")

name = input("> ")

print("Hello %s, welcome the the dungeon!" % (name))
print("Do you go through door 1 or door 2?")

def wrong_input():
    print("You are not so good with numbers, are you?")

# create function with an argument
def dead(death_message):
    print("You are dead.", death_message)

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
        # using function
        dead("Sorry %s, the vampire is faster. You become a dinner." % (name))
    else:
        wrong_input()

# GET CREATIVE:
# check if the input the user gave you is bigger/smaller than 50 with: if int(some_input) > 50

else:
    wrong_input()