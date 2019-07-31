while True:
    try:
        a = int(input("Enter a number for variable A: "))
        b = int(input("Enter a number for variable B: "))
    except ValueError:
        print("The value you entered is not valid, please enter a number.")
        continue
    else:
        break


def compare(x, y):
    if x < y:
        print("A is smaller than B")
    if x > y:
        print("A is bigger than B")
    if x == y:
        print("A is equal to B")


compare(a, b)
