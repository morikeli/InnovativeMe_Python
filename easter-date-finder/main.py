# Program to determine Easter date of a given year.
# The program uses Gauss Easter algorithm to determine the Easter date of a given year.
"""
    Program created by Mori Keli.
    Created: 16 Aug 2021 10:40 pm.
    © Mori Keli 2021 | All rights Reserved.
    
    Your feedback is highly appreciated.
"""

from logs.logger import create_log_file
import calendar
import math

def find_easter_date(year):
    """ This is an implementation of the Gauss Easter algorithm to determine the Easter date of a given year. """

    if year.isnumeric():
        Y = int(year)
        a = Y % 4   # find the no. of leap years according to Julian calendar.
        b = Y % 7   # non-leap years are one day longer than 52 weeks.
        c = Y % 19  # Calculate the location of the year 'Y' in Meonic cycle.

        C = int(year[:2])  # Century, e.g. 1900 -> C = 19 since the first two numbers are sliced out. C/100 will also work.
        m = (math.floor(15 + C - (C/4) - ((8 * C + 13)/25))) % 30
        n = (4 + C - (C/4)) % 7    # difference between the number of leap days between the Julian and Gregorian calendar.
        d = ((19 * c) + m) % 30  # no. of days to be added to March 21 to find the date of the Paschal full moon.
        e = ((2*a) + (4*b) + (6*d) + n) % 7   # no. of days from the Paschal full moon to the next Sunday.

        # Easter is either in March or April.
        day_march = 22 + d + e  # Easter on March.
        day_april = d + e - 9   # Easter on April.

        """
            Easter is either March(22+d+e) or April(d=e-9). There is an exception if d = 29 and e = 6. In this case, Easter 
            falls one week earlier on April 19. There is another exception if d = 28, e = 6, and m = 2, 5, 10, 13, 16, 21,
            24 or 39. In this case, Easter falls one week earlier on April 18.
        """

    # Exception 1: Easter falls one week earlier on 19th April.
        if d == 29 and e == 6:
            easter_date = f'19-04-{Y:02d}'  # Easter date of the given year.
            print(f'Easter date: {easter_date}')
            print(calendar.calendar(Y, 4))  # A calendar is printed with the month of April and year Y.

    # Exception 2: Easter falls one week earlier on 18th April.
        elif d == 28 and e == 6 and m == (2 or 5 or 10 or 13 or 16 or 21 or 24 or 39):
            easter_date = f'18-04-{Y:02d}'
            print(f'Easter Date: {easter_date}')
            print(calendar.calendar(Y, 4))

        # if march > 31 move Easter date to April.
        elif day_march > 31:
            easter_date = f'{day_april:02.0f}-04-{Y}'
            print(f'Easter date: {easter_date}')
            print(calendar.calendar(Y, 4))

        # Otherwise remain in March.
        else:
            easter_date = f'{day_march:02.0f}-03-{Y:02d}'
            print(f'Easter date: {easter_date}')
            print(calendar.calendar(Y, 3))  # A calendar is printed with the the month of March and year Y.

    return easter_date and create_log_file(easter_date)
    


if __name__ == '__main__':
    user_input = str(input('Enter a year: '))
    
    # Check if the year has 4 digits, its a numeric value and if its greater than year 2100.
    # Since it should have at least 4 digits, the least year by default will be year 1000.
    if ((len(user_input) != 4) and (user_input.isnumeric() is True)) or int(user_input) > 2100:
        print('INVALID INPUT!! Enter years between 1000 - 2100')
    
    else:
        find_easter_date(user_input)