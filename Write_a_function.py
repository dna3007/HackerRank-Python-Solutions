"""
Given a year, determine whether it is a leap year. If it is a leap year,
return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
It is only necessary to complete the is_leap function.
"""


def is_leap(_year):
    leap = False

    if _year % 4 == 0:
        leap = True
    if _year % 100 == 0:
        leap = False
        if _year % 400 == 0:
            leap = True
    return leap


year = int(input("Enter year : "))
print(is_leap(year))
