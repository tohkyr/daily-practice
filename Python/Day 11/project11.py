def main():
    check = input("Is your input a string or an integer? Type int for integer, str for string: ").lower()
    if check == "int":
        a = int(input("Enter the item you want to check: "))
    elif check == "str":
        a = str(input("Enter the item you want to check: "))
    else:
        print("That's not valid, try again")
        main()

    def nest():
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        class Checker(object):

            def __init__(self, item, list_check):
                self.item = item
                self.list_check = list_check

            def check(self):
                if self.item in self.list_check:
                    print("Item is in list.")
                else:
                    print("Item is not in list.")

            def restart(self):
                usr_int = input("Do you want to check for another item? Type Y to continue: ").lower()
                if usr_int == "y":
                    main()
                else:
                    exit()

        b = Checker(a, list)
        b.check(), b.restart()
    nest()

main()
