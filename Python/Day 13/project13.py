# Receive user input to select translation type.
def usr_input():
    user_input = str(input("Enter 1 if you want to translate to PygLatin, 2 if you want to translate PygLatin to English: "))
    if user_input == "1":
        translate_pyg_latin()
    elif user_input == "2":
        translate_to_english()
    else:
        print("Unresolved input, please try again.")
        usr_input()


# Re-run function if user wants to.
def retry():
    user_input = str(input("Do you want to translate again? y/n: ")).lower()
    if user_input == "y":
        usr_input()
    else:
        print("Thanks for using this program!")
        quit()


# Translate received input to PygLatin.
def translate_pyg_latin():
    lang_input = str(input("Enter what you want to translate: ")).split()
    translated = [word[1:] + word[0] + "ay" for word in lang_input]
    connected_sentence = " ".join(translated)
    print(connected_sentence)
    retry()


# Translated PygLatin input to normal.
def translate_to_english():
    pyg_input = str(input("Enter what you want to translate back: ")).split()
    pyg_translated = [word[-3] + word[:-3] for word in pyg_input]
    connected_sentence = " ".join(pyg_translated)
    print(connected_sentence)
    retry()


usr_input()

