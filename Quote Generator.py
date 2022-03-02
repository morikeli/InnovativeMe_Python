# Program to import quotes from the 'quotes' module and display quotes randomly. The quotes are displayed at each program is run.
"""
    Program created and maintained by Mori Keli.
    Created: 21 Aug 2021 06:15 pm.

    © Mori Keli 2021 | All rights Reserved. No part of this program shall be copied, altered or transferred to unspecified location without developer's
    consent. Failure to abide by this rule itafanya tukosane VIBAYA! VIBAYA SANA!!! Your feedback is highly appreciated.
"""
import os
from stat import S_IREAD
import quotes   # This is a user defined module that contains a list of quotes.
from random import choice
print('___'*30)
print('{:^80s}'.format('QUOTE OF THE DAY'))
print('---'*30)
print('{:^80s}'.format(choice(quotes.quote_lst)))   # choice randomly selects one quote to be displayed from the quote_lst.
print('==='*30)
os.chmod('quotes.py', S_IREAD)  # this code alters the 'quotes.py' to a read-only file.

try:    # The program tries to create a new text file and save it in the project folder if it does not exist else it will open the file for writing.
    f = open('program_data.txt', 'w')

    # The following strings and quotes will be printed in the 'program_data' text file.
    print('{:^80s}'.format('---PROGRAM DATA FILE---'), '\n', file=f)
    print('==='*30, file=f)
    print('{:^80s}'.format('QUOTE OF THE DAY'), file=f)
    print('~~~'*30, file=f)
    print('{:^100s}'.format(choice(quotes.quote_lst)), file=f)
    print('~~~'*30, file=f)
    print('{:^80s}'.format('*****END OF FILE*****'), file=f)

except FileNotFoundError:   # 'File Not Found' error message will be displayed if the text file location is changed
    print('\'program_data.txt\' NOT FOUND! It may have been deleted or moved to another location.')
except FileExistsError:     # This error will be raised if the program tries to create another text file of the same name.
    print('\'program_data.txt\' already exists in project file.')
finally:    # Once data is written into the file the program opens and closes the file.
    # f = open('program_data.txt')
    f.close()
