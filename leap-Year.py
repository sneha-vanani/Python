""" Check if a given year is a leap year or not."""
"""a year is a leap year if it is divisible by 4, unless it is divisible by 100 but not by 400. This logic is implemented using the modulo operator (%), which returns the remainder of a division. """

def is_leap(year):

    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        return True
    return False

y = int(input("Enter a year: "))
if is_leap(y):
    print("leap year")
else:
    print("not leap year")