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


# GET CREATIVE:
# Write a function for your_room


def dead(why):
    print(why, "You are dead.")
    exit(0)

start()