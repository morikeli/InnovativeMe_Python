"""
    2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged, maintained by Mori Keli.
    Created 06/03/2022 15:40 EAT
"""

# Program to print a number of random characters
from time import sleep
from string import *
from random import sample
i = 0
j = 0
while i == 0:
    char_str = str(digits)+punctuation+ascii_lowercase+ascii_uppercase+hexdigits+octdigits
    len_char = len(str(digits) + punctuation + ascii_lowercase + ascii_uppercase + hexdigits + octdigits)
    joined_str = ''.join(sample(char_str, len_char))

    # print joined_str 10 times before executing an infinite loop
    for i in range(10):
        sleep(1)    # pause for a second before printing the value of joined_str
        print(joined_str)

    while j == 0:   # an infinite while loop
        print(joined_str)
