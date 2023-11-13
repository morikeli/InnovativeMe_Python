"""
    2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli
    Created 06/03/2022 14:39 EAT

"""
# Program to display random characters generated from string module.

from random import sample
from string import (ascii_letters as letters, 
        ascii_lowercase as lowercase_letters, 
        digits, hexdigits as hexd, 
        punctuation as p, 
        whitespace as w,
    )


def print_infinity_loop_with_random_characters():
    """ This function prints random characters on your terminal. """
    
    while True:
        joined_str = ''.join(sample(letters + hexd + digits + lowercase_letters + p, len(digits + lowercase_letters + hexd + w)))
        text_str = f"Hello, its me again! What if scared your CPU ... {joined_str} HA!HA!HA! ..."

        print(text_str)
    

if __name__ == '__main__':
    print_infinity_loop_with_random_characters()
