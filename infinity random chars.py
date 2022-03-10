"""
    2022 MORI KELI | ALL ROGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created 06/03/2022 15:59 EAT
"""
# Program to print a number of random characters
from time import sleep
from string import *
from random import sample, shuffle

i = 0
j = 0
k = 0
while i == 0:
    char_str = str(digits)+punctuation+ascii_lowercase+ascii_uppercase+hexdigits+octdigits
    # len_char = len(str(digits) + punctuation + ascii_lowercase + ascii_uppercase + hexdigits + octdigits)
    len_char = len(char_str)
    joined_str = ''.join(sample(char_str, len_char))

    # print value of joined_str 10 times before executing an infinite loop
    for i in range(10):
        sleep(1)    # pause for a second before printing value of "joined_str"
        print(joined_str)

    # Infinite loop
    while j == 0:
        # convert joined str to a list to use shuffle function since it does not work with strings.

        for i in range(1):
            print('\n\n')
            print('Prepare for your worst nightmare ... HA!HA!HA!\n\n')
        sleep(5.5)   # delay execution for 5.5 seconds

        while k == 0:
            convert_str = list(joined_str)
            shuffle(convert_str)
            print(''.join(convert_str))    # print a shuffled joined_str; the value of joined_str is different from the initial joined_str
            # sleep(1)
