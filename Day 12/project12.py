list_1 = []
list_2 = []


def list_clear():
    list_1.clear()
    list_2.clear()


def list_get():
    element_number_1 = int(input("Enter the number of elements for list 1: "))
    element_number_2 = int(input("Enter the number of elements for list 2: "))

    for e1 in range(0, element_number_1):
        element_add_1 = input("Enter what you want to add to list 1: ")
        list_1.append(element_add_1)

    for e2 in range(0, element_number_2):
        element_add_2 = input("Enter what you want to add to list 2: ")
        list_2.append(element_add_2)

    print("list 1: " + str(list_1))
    print("list 2: " + str(list_2))

    correct_list = input("Is these lists correct? y/n: ")
    if str(correct_list) == "y":
        print("OK, list acquired.")
        print("Connecting lists...")
        list_connect()
    else:
        list_clear()
        list_get()


def list_connect():
    connect = list_1 + list_2
    print("Lists connected. List: " + str(connect))


list_get()
