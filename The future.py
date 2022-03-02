""" Program written by: Mori Keli
    Date: 06/2/2021
    All rights reserved. No part of this code may be altered, printed or copied without my permission.
    Ukijaribu TUTAKOSANA VIBAYA SANA!!!!!!
"""
# Write a program that asks the user how many hours he/she wants to go into the future.
# The program asks the user for an hour between 1 and 12 and asks them to enter time in am or pm.
# The program also asks the user how many hours into the future they want to go.

time = int(input('Enter an hour between 1 and 12: '))
if time<1 or time>12:
    print('ERROR!!! This program only supports 12-hour clock system. Please try again.')
else:
    t_format = input(str('For am enter 1 and for pm enter 2: '))
    if t_format == 1 or t_format ==2:
        print('INVALID CHOICE!!! Please try again. For time in \'am\' enter 1, for time in \'pm\' enter 2.')
    else:
        future = int(input('How many hours do you want to go into the future: '))


# The program only supports 12-hour clock system. 24-hours time format is converted back into 12-hour clock system.

        if (future+time)>12 or t_format == 1:
            print('New hour: ', (future+time)-12, 'pm')     # time is converted back into 12-hour clock system(am-pm).
        elif (future+time) == 12 or t_format == 1:
            print('New hour: ', (future+time), 'pm')
        elif (future+time)>12 or t_format == 2:
            print('New hour: ', (future+time)-12, 'am')     # time is converted back into 12-hour clock system(pm-am).
        elif (future+time) == 12 or t_format == 2:
            print('New hour: ', (future+time), 'am')
        elif (future+time) % 12 != 0 or t_format == 1:
            print('New hour: ', (future+time), 'am')
        elif (future+time) < 12 or t_format == 2:
            print('New hour: ', (future+time), 'pm')

