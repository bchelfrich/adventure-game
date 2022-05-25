# Continuing my decision-based adventure typing game to practice my Python skills.
# Author: Brandon Helfrich

import sys
import time

# Defining a typing text effect for the print() function
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)


# Defining a typing text effect for the input() function
def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)
    value = input()
    return value


# START OF FOREST

time.sleep(3)

typingPrint("The Dark Forest, as it's known those inside of the walls, is the home of many dark creatures.\n")
