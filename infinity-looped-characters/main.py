"""
    2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged, maintained by Mori Keli.
    Created 06/03/2022 15:40 EAT
"""

# Program to print a number of random characters
# My goal was to mimic scenes in hacking movies where a hacker usually has one desktop screen displaying random characters on their idle desktop screens. The characters move from bottom of the screen to the top of the screen in slow motion, i.e. line by line.
 
from time import sleep
from string import (ascii_letters as letters,
        ascii_lowercase as lowercase_letters,
        ascii_uppercase as uppercase_letters, 
        digits, 
        hexdigits,
        octdigits,
        punctuation,
        whitespace,
    )
from random import sample


DIGITS = digits
HEXADECIMAL_DIGITS = hexdigits
LOWERCASE_LETTERS = lowercase_letters
LETTERS = letters
OCTALDIGITS = octdigits
SYMBOLS = punctuation
UPPERCASE_LETTERS = uppercase_letters
WHITESPACE = whitespace


def generate_infinity_loop():
    while True:
        characters_str = DIGITS + HEXADECIMAL_DIGITS + LOWERCASE_LETTERS + LETTERS + OCTALDIGITS + SYMBOLS + UPPERCASE_LETTERS + WHITESPACE   # concatenate all characters
        length_chars = len(DIGITS + HEXADECIMAL_DIGITS + LOWERCASE_LETTERS + LETTERS + OCTALDIGITS + SYMBOLS + UPPERCASE_LETTERS + WHITESPACE)    # length of all characters
        joined_str = ''.join(sample(characters_str, length_chars))

        # generate a new set of characters after 10 iterations.
        for i in range(10):
            sleep(0.5)    # pause for half a second (i.e 5ms) before printing random characters
            print(joined_str)


if __name__ == '__main__':
    generate_infinity_loop()