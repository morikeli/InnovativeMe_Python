# Program to display the length no. of characters, digits and words in a string.
"""
    Program created and maintained by Mori Keli.
    Created: 19 Aug 2020 08:00 pm.

    © Mori Keli 2021 | All rights Reserved. No part of this program shall be copied, altered or transferred to unspecified location without developer's
    consent. Failure to abide by this rule itafanya tukosane VIBAYA! VIBAYA SANA!!! Your feedback is highly appreciated.
"""
import os
import p_time
from stat import S_IREAD
print(p_time.p_format())
txt = str(input('Type your text here...\n'))
char = 0
dgt = 0
let = 0
wrd = 1
for i in txt:
    char += 1   # variable char counts the number of characters in a string 'txt'.
    if i.isnumeric():
        dgt += 1    # dgt variable counts the number of digits in the string 'txt'.
    elif i.isspace():
        wrd += 1   # variable wrd counts the number of words in the string 'txt'.

print('~~~'*50)
print('Text: {:<s} \n'.format(txt))
print('---'*50)
if len(txt) == 1:
    let += 1
    print('{:^130s}'.format('Your text has {:,d} character(s), {:,d} digit(s) and {:,d} letter(s).'.format(char, dgt, let)))    # will be printed if the user
    # types a letter
elif len(txt) == 0:
    print('{:^130s}'.format('YOUR TEXT IS BLANK!!'))
else:
    print('{:^130s}'.format('Your text has {:,d} character(s), {:,d} digit(s) and {:,d} word(s).'.format(char, dgt, wrd)))
print('~~~'*50)

path = 'C:/users/MORI/OneDrive/Documents/Coding/Python/Program to count the number of characters, digits and words in a string/data.txt'

try:
    os.chmod('data.txt', 0o0755)    # the read-only property is removed before the file is opened for writing.
    f = open(path, 'w')
    print('{:^80s}'.format('---PROGRAM DATA---'), file=f)
    print('---'*30, file=f)
    print('{:^80s} \n{:s}'.format('Text', txt), file=f)
    print('===' * 30, file=f)
    print('{:^80s}'.format('Your text has {:,d} character(s), {:,d} digit(s) and {:,d} word(s).'.format(char, dgt, wrd)), file=f)
    print('===' * 30, file=f)
    print('{:^80s}'.format('*****END OF FILE*****'), file=f)

except FileExistsError:
    print('File already exists!!')
except FileNotFoundError:
    print('File Not Found!! The file may have been moved to another location.')
finally:
    f = open(path)
    os.chmod('data.txt', S_IREAD)   # data txt is converted into a read-only text file.
    f.close()
