
a = input("ENTER A NUMBER: ")
b = input("ENTER b NUMBER: ")

if a.isdigit() and b.isdigit():
    if a > b:
        print("A is larger than B")
    if a < b:
        print("A is smaller than B")
    if a == b:
        print("A is equal to B")
else:
    print("A or B is not a number!")
