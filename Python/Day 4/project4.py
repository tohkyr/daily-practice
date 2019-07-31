while True:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("That's not a number!")
        continue
    else:
        break

def sumcalc(n):
    print(sum(range(n+1)))

sumcalc(n)