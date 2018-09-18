"""
Task 7

Use the dictionary adventure below to control the game play instead of if-else statements.

This task combines for-loops, complex dictionaries and lists. It is recommended after the
concepts of loops and dictionaries and lists are pretty well understood.

In the code below there a complex dictionary named `adventure` that has as values dictionaries as well.
This complex dictionary includes all the text needed to play the game. The value of a door eg door '1' is
also a dictionary, with keys "greeting" that is the text to show when the user enters the room and
"options" which is a list of dictionaries with the "action" to display and then the "result" to show to the
user when they choose this option. Currently only the door 1 is defined.


A. Take some time to understand the structure of the dictionary adventure in the code below. Copy this code to a new file
and continue the program in the indicated line and print the greeting of the chosen door,
using the value from the dictionary
 eg. the greeting of the door '1' can be accessed with adventure['1']['greeting'] or if the
 door number is in a variable called door, adventure[door]['greeting'] will get the greeting for the
 variable door from the dictionary. This value can be passed directly into a print statement.

B. Exactly after the print of the greeting print the possible actions for each option of the chosen door. Eg.
Options:
 1. Smile and node
 2. Scream and run
Tips:
    * Accessing the action of the first option of the first door can be done with adventure['1']['options'][0]['action']
    * For loop is needed to go through the list of options.
    * To show the number of each option python enumerate function can be useful,
    http://book.pythontips.com/en/latest/enumerate.html


C. Add more options to door '1'.
D. Add more doors to adventure dictionary.
Tip: Copy paste the structure of door '1' and change the values.

E. If the chosen door is not available in adventure show a message.
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
            },
            # Exercise C
        ]
    },
    # Exercise D
}


print("Which door do you choose" + '/'.join(adventure.keys()) + "?")  # join() is python method to make one string out of a list of things
                                                                      # adventure.keys() is a list with all the dictionary keys, in that
                                                                      # case is only door ['1']

door = input("> ")

# Exercise A - print greeting to the chosen door

# Exercise B - print user options with their number

# Exercise C - if the door is not in the available options print a message

