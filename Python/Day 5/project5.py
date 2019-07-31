while True:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("That's not a number!")
        continue
    else:
        break

def oddcalc(n):
    for num in range(n+1):
        if num % 3 == 0 or num % 5 == 0:
            print(num)

oddcalc(n)
