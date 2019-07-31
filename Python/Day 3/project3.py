while True:
    try:
        name = input("Enter your name: ")
        if name == "Alice" or name == "Bob":
            print("Welcome " + name + "!")
            break
        else:
            print("That's not the correct name!")
    except:
        print("An excception occured.")






