usr_input = input("Enter your list element seperated by a , : ")

list1 = usr_input.split(", ")

def long_print(list):
    print(max(list, key=len))

long_print(list1)
