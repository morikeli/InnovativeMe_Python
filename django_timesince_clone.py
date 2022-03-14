"""
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged and maintained by Mori Keli.
    Created: 27/2/2022 15:00 EAT
"""
# Program to print remaining days and hours left from a string.
# I used this program to imitate the 'timesince' tag in Django.
from datetime import datetime
d = datetime.today()
print('Current Date: ', d)
d1 = "2022-02-28"
# print(int(d1)-int(d))
due = datetime.strptime(d1, "%Y-%m-%d")
result = due-d

if result.days < 0:     # checks if the date selected is a past date, e.g. previous year, month
    print('Selected a past date')
    exit(1)
else:
    print('Days left: {:02d} days left'.format(result.days))   # prints days remaining
    print('Time Left: {}'.format(result))   # prints days left and time in hours, minutes, seconds
try:
    # create a text file and save data into the text file.
    txt_file = open('data.txt', 'a')
    print('Days left: {}'.format(result), file=txt_file)
except FileNotFoundError:
    print('Data cannot be copied to a text file! "data.txt" may have been deleted or moved to another location.')
except FileExistsError:
    print('"data.txt" already exists in the project folder.')
finally:
    txt_file = open('data.txt', 'w')
    txt_file.close()
