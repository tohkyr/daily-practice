import calendar


start_year = input("Enter start year: ")
while not start_year.isdigit():
    start_year = input("That's not a number, please try again: ")


num_years = input("Enter how many years ahead you want to check: ")
while not num_years.isdigit():
    start_year = input("That's not a number, please try again: ")

start = int(start_year)
num = int(num_years)

def leap_print(year, number_of_years):
    year_checked = 0
    while year_checked < number_of_years:
        if calendar.isleap(year):
            print(year)
            year_checked += 1
        year += 1


leap_print(start, num)
