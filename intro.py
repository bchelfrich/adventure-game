# Making a long, but simple decision-based typing adventure game to practice my Python.
# Author: Brandon Helfrich

import sys
import time   # time.sleep() function pauses the program in between lines to simulate the feel of a "terminal game."

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


# START OF INTRO

name = input("Name your character: ")
name = name.capitalize().strip()   # .capitalize().strip() function will auto capitalize the name & strip of spaces.
print()

time.sleep(1)

typingPrint("You awaken in a cold, damp cell. The feint squeaks of rats and water dripping on stone \n")
typingPrint("echoes in the dark.\n\n")

time.sleep(1)

typingPrint("Footsteps approach your cell and a raspy voice whispers out.\n\n")

time.sleep(1)

print("Voice :")
typingPrint("'Do you know who I am?'\n\n")

time.sleep(1)

# This typing game is decision-based and is heavily built on 'While True' loops.
while True:
    answer = input("([Y] for yes | [N] for no): ").lower().strip()   # .lower().strip() function will auto lowercase
    print()                                                          # input & strip of spaces. Useful in many cases
    if answer == "y":                                                # throughout this program.

        time.sleep(1)

        print(name, ": ")
        typingPrint("'Yes, Your Grace.'\n\n")

        time.sleep(1)

        print("The King :")
        typingPrint("'Then you must be very confused. I have seen a prophecy, and you at the center of it. I do \n ")
        typingPrint("not know what it means but I must get you out of here.'\n\n")
        break

    if answer == "n":

        time.sleep(1)

        print(name, ":")
        typingPrint("'I can't see a thing in here. Who are you?'\n\n")

        time.sleep(1)

        print("The King :")
        typingPrint("'I am the King, and I have seen a prophecy of great destruction to this land. I do not know \n")
        typingPrint(" why, but you are the only one who can stop it. I must get you out of here.'\n\n")
        break

    print("Invalid choice. Try again!")   # Will loop until you give a valid answer.

time.sleep(1)

typingPrint("The King unlocks your cell and walks in, closing the door behind him.\n\n")

time.sleep(1)

print("The King :")
typingPrint("'There is a much bigger picture. When you were falsely put in here, I could not interfere as the Lords \n")
typingPrint(" wouldn't get behind the foolery of a prophecy. I fear whoever arranged you to be put in here knows of \n")
typingPrint(" the prophecy and will be making sure you don't fulfill it.'\n\n")

time.sleep(1)

typingPrint("The King pushes in a block of stone and a secret tunnel behind the wall is revealed.\n\n")

time.sleep(1)

print("The King :")
typingPrint("'Follow this tunnel and it will lead you through the sewer system and outside of the city. \n")
typingPrint(" I was never here...'\n\n")

time.sleep(1)

typingPrint("How will you respond?\n")

time.sleep(1)

while True:
    answer = input("([Y] for correspondence | [N] for resistance): ").lower().strip()
    print()
    if answer == "y":

        time.sleep(1)

        print(name, ":")
        typingPrint("'Yes, Your Grace. I will not fail you.'\n\n")
        break

    if answer == "n":

        time.sleep(1)

        print(name, ":")
        typingPrint("'This is blasphemy. I will have no part in whatever charade this is. You look absolutely \n")
        typingPrint(" nothing like his Majesty. Leave at once!'\n\n")

        time.sleep(1)

        typingPrint("You spend the rest of your days rotting in your cell until an incredibly bright light \n")
        typingPrint("shreds across the sky, and everything around you bursts to flames.\n\n")

        time.sleep(1)

        typingPrint("You have died.")
        exit()
        break

    print("Invalid choice. Try again!")

time.sleep(3)

typingPrint("You are walking along the sewer path and you reach a crossroads.\n")

time.sleep(1)

while True:
    answer = input("([L] for left | [R] for right): ").lower().strip()
    print()
    if answer == "l":

        time.sleep(1)

        typingPrint("You encounter a monster. You have no weapon.\n")

        time.sleep(1)

        while True:
            answer = input("([A] for attack | [R] for run): ").lower().strip()
            print()
            if answer == "a":

                time.sleep(1)

                typingPrint("That wasn't a good idea.\n")

                time.sleep(1)

                typingPrint("You have died.")
                exit()
                break

            if answer == "r":

                time.sleep(1)

                typingPrint("You run past the monster, but now it is chasing you. It is gaining on you.\n")

                time.sleep(1)

                while True:
                    answer = input("([H] for hide | [P] for panic): ").lower().strip()
                    print()
                    if answer == "p":

                        time.sleep(1)

                        typingPrint("You panic and scream for help. The monster grabs you by the legs and pulls \n")
                        typingPrint("you back.\n")

                        time.sleep(1)

                        typingPrint("You have died.")
                        exit()
                        break

                    if answer == "h":

                        time.sleep(1)

                        typingPrint("You see a barrel ahead and decide to hide under it.\n")

                        time.sleep(1)

                        typingPrint("You successfully evaded the monster.\n\n")

                        time.sleep(1)

                        break

                    print("Invalid choice. Try again!")

                break

            print("Invalid choice. Try again!")

        typingPrint("You see a hole in the ground with a ladder going down, deeper into the network. \n\n")

        break

    if answer == "r":

        time.sleep(1)

        typingPrint("You are walking down the path and start to hear a clicking sound.\n")
        typingPrint("You turn around to see a massive arachnid.\n\n")

        time.sleep(1)

        typingPrint("What will you do?\n")

        while True:
            answer = input("([A] for attack | [R] for run): ").lower().strip()
            print()
            if answer == "a":

                time.sleep(1)

                typingPrint("You see a large broken piece of wood nearby on the ground and quickly impale the \n")
                typingPrint("creature in the center.\n")

                time.sleep(1)

                typingPrint("You have successfully killed the arachnid.\n\n")

                time.sleep(1)

                break

            if answer == "r":

                time.sleep(1)

                typingPrint("You attempt to flee from the arachnid but you feel a powerful web tangle you by \n")
                typingPrint("the legs and pull you back. You have become his meal.\n\n")

                time.sleep(1)

                typingPrint("You have died.")
                print()

                break

            print("Invalid choice. Try again!")

        typingPrint("You walk past the fallen beast and see a hole in the ground with a ladder going down, \n")
        typingPrint("deeper into the network.\n\n")

        break

    print("Invalid choice. Try again!")


time.sleep(3)

typingPrint("You continue down the path until you start to hear a faint groaning sound.\n")
typingPrint("A frail old man sits on a pipe. His hair and beard nearing his knees.\n\n")

time.sleep(1)

print("Man :")
typingPrint("'So, another seeks passage to his freedom, hmm?'\n\n")

time.sleep(1)

print(name, ":")
typingPrint("'Excuse me?'\n\n")

time.sleep(1)

print("Man :")
typingPrint("'Many before you have made mistakes to end up in the place you come from. \n")
typingPrint(" Many before you have grown tired of its conditions and found the passages \n")
typingPrint(" placed for their escape. All would end up lost in the network of tunnels if \n")
typingPrint(" it were not for me. I can guide you, but you must answer a riddle.'\n\n")

time.sleep(1)

typingPrint("Do you accept?\n")
while True:
    answer = input("([Y] for yes | [N] for no): ").lower().strip()
    print()
    if answer == "n":

        time.sleep(1)

        print(name, ":")
        typingPrint("'I am not a child and I do not have time for your games.'\n\n")

        time.sleep(1)

        typingPrint("You continue through the network but find the old fool was right.\n")
        typingPrint("No matter how much you retrace your steps, you can't find your way \n")
        typingPrint("back. You search for what seems like an eternity until the monster \n")
        typingPrint("you evaded before corners you for his revenge.\n\n")

        time.sleep(1)

        typingPrint("You have died.")
        exit()
        break

    if answer == "y":

        time.sleep(1)

        print(name, ":")
        typingPrint("'Alight, fine. I will play your silly game. What is the riddle?'\n\n")

        time.sleep(1)

        print("Man :")
        typingPrint("'Be careful! You get one chance or your corpse shall fill my belly. \n")
        typingPrint(" It has been so long since I've had a good meal! So here goes: \n\n")
        typingPrint(" What comes once in a minute, twice in a moment, but never in a \n")
        typingPrint(" thousand years?'\n\n")

        time.sleep(1)

        while True:
            answer = typingInput("What is your answer? ").lower()
            print()
            if answer == "m":
                break
            if answer == "letter m":
                break
            if answer == "the letter m":
                break
            typingPrint("'Wrong!'\n\n")

            time.sleep(1)

            typingPrint("The old man slashes your throat.\n")

            time.sleep(1)

            typingPrint("You have died.")
            sys.exit()

        time.sleep(1)

        print("Man :")
        typingPrint("'Correct! I will grant you safe passage to your freedom!'\n\n")
        break

    print("Invalid choice. Try again!")

    time.sleep(1)

typingPrint("The old man guides through what seems like a maze of tunnels until you reach \n")
typingPrint("the large mouth of a cave. You can see the light of day in the distance.\n\n")

time.sleep(1)

print("Man :")
typingPrint("'I'm afraid this is where I must leave you. Once you get out, you will be outside of the city. \n")
typingPrint(" Be warned, though. There is little to save you outside the walls.'\n\n")

time.sleep(1)

typingPrint("The man bows and walks back into the tunnels. You begin to walk towards the light until a \n")
typingPrint("deafening screeching sound bellows throughout the cave.\n\n")

time.sleep(3)

typingPrint("From the shadows, a dragon shows his head. His pure black scales contrasted his bright eyes, \n")
typingPrint("which looked as if they were made of fire.\n\n")

time.sleep(1)

print("Dragon :")
typingPrint("'I have seen your face, Protector. The only reason I don't burn you where you stand is because \n")
typingPrint(" I enjoy a good fight. We will meet again, I assure you.'\n\n")

time.sleep(1)

typingPrint("The dragon opens his mouth and shoots a massive blast of fire at the tunnel entrance behind you, \n")
typingPrint("sealing the passage. His magnificent wings stretch, and he takes off.\n\n")

typingPrint("By the time you reach the outside of the cave, he is but a speck in the sky.\n\n")

time.sleep(3)

typingPrint("The light beams down and nearly blinds you. It has been so long since you've seen the sun.\n")
typingPrint("A path lies before you, leading into the forest that outlines the city walls.\n")
typingPrint("Your journey starts now.\n\n")

# END OF INTRO
