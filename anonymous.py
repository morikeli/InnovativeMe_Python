# Program to encrypt username
# Applicable in a crime reporting website for anonymity.

from string import ascii_letters
from random import sample

s = ascii_letters
special_char = '!@%*&$?'
myname = 'Username'

print('Your name: {}'.format(myname))

for c in myname:
    myname += c
    new_f = c.replace(c, ''.join(sample(s+special_char, len(myname))))

    print('{}'.format(new_f), end='')
