"""
Task 7

Use the dictionary adventure below to control the game play.

A. Continue the program in the indicated line and print the greeting to the chosen door.
Tip: Since now adventure['1'] is a dictionary you can use adventure['1']['greeting'] or
adventure['1']['options'] to get the values of that part.

B. Print after the greeting the possible actions for each option of the chosen door. Eg.
Options:
 1. Smile and node
 2. Scream and run
Tip: For loop is needed to go through the list of options. To show the number of each option python enumerate
function can be useful, http://book.pythontips.com/en/latest/enumerate.html

C. If the chosen door is not available in adventure show a message.
Tip to check if a value is one of the dictionary keys, the "in" or the "not in" can be used.
eg. if door in adventure
"""

adventure = {
    '1': {
        "greeting": "There is a nice vampire asking you if you enjoy life. What do you do?",
        "options": [
            {
                "action": "Smile and nod",
                "result": "Congratulations, you found a new friend!"
            },
            {
                "action": "Scream and run",
                "result": "Sorry the vampire is faster, you are dead!"
            },]},

}


print("Which door do you choose" + '/'.join(adventure.keys()) + "?")

door = input("> ")

# Exercise A - print greeting to the chosen door

# Exercise B - print user options with their number

# Exercise C - if the door is not in the available options print a message

