# Continuing my decision-based adventure typing game to practice my Python skills.
# Author: Brandon Helfrich

# import intro   # Adds the introduction. If you want to play, run this file.
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
typingPrint("It borders the Great City walls to keep enemies out, but also those who live within from curiosity.\n\n")

time.sleep(1)

typingPrint("You instantly feel the eeriness as you enter the shadows, you feel as if there are a thousand eyes\n")
typingPrint("on you, watching, waiting...\n")

time.sleep(1)

typingPrint("You reach a crossroads in the forest. Will you go left or right?\n")

while True:
    answer = input("([L] for left | [R] for right): ").lower().strip()
    print()
    if answer == "l":

        time.sleep(1)

        typingPrint("You have found a weapon! A dulling sword lies on the ground ahead, blood tried on the handle.\n")
        break

    if answer == "r":

        time.sleep(1)

        typingPrint("You have found a weapon! A dulling sword lies on the ground ahead, blood tried on the handle.\n")
        break

    print("Invalid choice. Try again!")
