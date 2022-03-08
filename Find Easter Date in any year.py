# Program to determine Easter date of a given year.
# The program uses Gauss Easter algorithm to determine the Easter date of a given year.
"""
    Program created by Mori Keli.
    Created: 16 Aug 2021 10:40 pm.

    © Mori Keli 2021 | All rights Reserved. No part of this program shall be copied, altered or transferred to unspecified location without developer's
    consent. Failure to abide by this rule itafanya tukosane VIBAYA! VIBAYA SANA!!! Your feedback is highly appreciated.
"""

import calendar
import math
yr = input('Enter a year: ')
if yr.isdigit():    # if the year is a digit, the program executes the program statements after the 'if' function.
    Y = int(yr)  # Converts string in variable yr to an integer.
    a = Y % 4   # find the no. of leap years according to Julian calendar.
    b = Y % 7   # non-leap years are one day longer than 52 weeks.
    c = Y % 19  # Calculate the location of the year 'Y' in Meonic cycle.

    C = int(yr[:2])  # Century, e.g. 1900 -> C = 19 since the first two numbers are sliced out. C/100 will also work.
    m = (math.floor(15 + C - (C/4) - ((8*C+13)/25))) % 30
    n = (4+C-(C/4)) % 7    # difference between the number of leap days between the Julian and Gregorian calendar.
    d = ((19*c)+m) % 30  # no. of days to be added to March 21 to find the date of the Paschal full moon.
    e = ((2*a)+(4*b)+(6*d)+n) % 7   # no. of days from the Paschal full moon to the next Sunday.

    # Easter is either in March or April.
    march = 22+d+e  # Easter on March.
    april = d+e-9   # Easter on April.

    """
        Easter is either March(22+d+e) or April(d=e-9). There is an exception if d = 29 and e = 6. In this case, Easter 
        falls one week earlier on April 19. There is another exception if d = 28, e = 6, and m = 2, 5, 10, 13, 16, 21,
         24 or 39. In this case, Easter falls one week earlier on April 18.
    """

# Exception 1:
    if d == 29 and e == 6:
        print('Easter date: {:02d}-{:02d}-{:04d}'.format(19, 4, Y))
        print(calendar.calendar(Y, 4))  # A calendar is printed with the month of April and year Y.

# Exception 2:
    elif d == 28 and e == 6 and m == (2 or 5 or 10 or 13 or 16 or 21 or 24 or 39):
        print('Easter Date: {:02d}-{:02d}-{:04d}'.format(18, 4, Y))
        print(calendar.calendar(Y, 4))

    # if march > 31 move Easter date to April.
    elif march > 31:
        print('Easter date: {:02.0f}-{:02d}-{:04d}'.format(april, 4, Y))
        print(calendar.calendar(Y, 4))

    # Otherwise remain in March.
    else:
        print('Easter date: {:02.0f}-{:02d}-{:02d}'.format(march, 3, Y))
        print(calendar.calendar(Y, 3))  # A calendar is printed with the the month of March and year Y.

else:
    print('Invalid input')  # if the entered year is not a digit, an error message is displayed.
