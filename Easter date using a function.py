# Function that returns Easter date of a given year.
import calendar   # import calendar to print March or April of year Y.
import math  # Useful for floor division.
Y = int(input('Enter a year: '))    # The user enters a year.


def gaussEaster(y):
    a = Y % 4  # find the no. of leap years according to Julian calendar.
    b = Y % 7  # non-leap years are one day longer than 52 weeks.
    c = Y % 19  # Calculate the location of the year 'Y' in Metonic cycle.

    C = Y/100
    m = (math.floor(15 + C - (C / 4) - ((8 * C + 13) / 25))) % 30
    n = (4 + C - (C / 4)) % 7  # difference between the number of leap days between the Julian and Gregorian calendar
    d = ((19 * c) + m) % 30  # no. of days to be added to March 21 to find the date of the Paschal Full moon.
    e = ((2 * a) + (4 * b) + (6 * d) + n) % 7

    # math.floor(m)
    march = 22 + d + e  # Formula to determine Easter date on March.
    april = d + e - 9   # Formula to determine Easter Date on April.

    calendar.setfirstweekday(6)   # Set Sunday(6) as the first day of week when the calendar is printed.
# Exception 1:
    if d == 29 and e == 6:
        print('Easter Sunday: {:02d}-{:02d}-{:04d}'.format(19, 4, Y))
        print('\n', calendar.calendar(Y, 4))    # prints calendar for April in the year Y.
        return
# Exception 2:
    elif d == 28 and e == 6 and m == (2, 5, 10, 13, 16, 21, 24, 39):
        print('Easter Sunday: {:02d}-{:02d}-{:04d}'.format(18, 4, Y))
        print('\n', calendar.calendar(Y, 4))
        return

    # if the days in march>31 move to April.
    elif march > 31:
        print('Easter Sunday: {:02.0f}-{:02d}-{:04d}'.format(april, 4, Y))
        print('\n', calendar.month(Y, 4))
        return
    # Otherwise, stay on March.
    else:
        print('Easter date: {:02.0f}-{:02d}-{:04d}'.format(march, 3, Y))
        print('\n', calendar.month(Y, 3))   # prints calendar for March for year Y.
        return


gaussEaster(Y)
