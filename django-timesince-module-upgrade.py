"""
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged and maintained by Mori Keli.
    Created: 27/2/2022 15:00 EAT

    Django-"timesince"-util clone version 1.1
"""
# Updated version of Django 'timesince' utility clone
from datetime import datetime
current_date = datetime.today()
# selected_date = str(input('Enter date in yyyy/mm/dd" format: '))
selected_date = "10-03-2022"    # 10th March 2022
due_date = datetime.strptime(selected_date, "%d-%m-%Y")
days_left = due_date - current_date
time_left = days_left

if days_left.days < 0:
    print('You have lived past the selected date.')     # for example dates 2015-01-31 or 2022-01-20 or 2022-02-26 will display this message

    # try creating a text file to save the above data.
    try:
        txt_data_file = open('data.txt', 'w')
        print('You have lived past the selected date.', file=txt_data_file)
    except FileNotFoundError:
        print('"data.txt" not found:: file may have been deleted or moved to another location.')
    except FileExistsError:
        print('File with same name "data.txt" already exists!')
    finally:
        txt_data_file = open('data.txt', 'r')   # open the text file for reading purposes.
        txt_data_file.close()   # close the text file once data has been written and saved into the file.
else:
    print('Current date: {}'.format(current_date))
    print('Date Entered: {}'.format(selected_date))
    print('Days left: {} days'.format(days_left.days))

    # save the data in a text file
    try:
        txt_data_file = open('data.txt', 'w')
        print('You have lived past the selected date.', file=txt_data_file)
    except FileNotFoundError:
        print('"data.txt" not found:: file may have been deleted or moved to another location.')
    except FileExistsError:
        print('File with same name "data.txt" already exists!')
    finally:
        txt_data_file = open('data.txt', 'r')
        txt_data_file.close()
