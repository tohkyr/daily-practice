import os
import webbrowser


def automate():
    day = input("Enter day number: ")
    while not day.isdigit:
        day = input("That is not a number, try again: ")

    path = "D:/Coding/Day " + str(day)
    os.mkdir(path)
    readme = open("D:/Coding/Day " + str(day) + "/README.md", mode='w')
    challenge = input("Enter challenge description: ")
    learned = input("Enter what you've learned: ")
    readme.write("""# Day {}

**Day {}:** {}

**What I learned:** {} """.format(day, day, challenge, learned))

automate()
