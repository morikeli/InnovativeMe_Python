"""
    This is a simple number guessing game.

    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created 11/03/2022 05:35 EAT
"""
from random import randint
from logs.logger import create_data_log

def guess_a_number(number, guess=0):
    num = randint(1, number)

    while guess != num:
        try:    # try to verify if the entered  value is an integer.
            guess = int(input('Enter a number between 1 and {}: '.format(number)))

        except ValueError:  # if not an integer, print the following statement and terminate the program.
            print('Sorry, {} is not an integer.'.format(guess))
            exit(1)

        if guess < num:
            print('Too low! Please try again.')
        elif guess > num:
            print('Too high! Please try again.')

    print('Hurray! You have guessed the number {:02d} correctly!'.format(num))
    return create_data_log(guess)


if __name__ == '__main__':
    guess_a_number(10)