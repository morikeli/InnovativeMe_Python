"""
    2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli
    Created 06/03/2022 14:39 EAT

"""
# Program to display random characters generated from string module.

from random import sample
from string import *

i = 0
while i == 0:
    print('Hello, its me again! What if ...')

    d = digits
    lett_lower = ascii_lowercase
    x = hexdigits
    letters = ascii_letters
    w = whitespace
    p = punctuation
    print('{} {}'.format(''.join(sample(lett_lower + x + str(d) + letters + p, len(str(d) + lett_lower + x + letters + p))), 'was a ...'))

# The program displays the following statement:
# "Hello, its me again! What if ... {random characters} was a ..."
