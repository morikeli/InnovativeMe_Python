"""
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created 11/03/2022 05:35 EAT
"""
from random import randint


def your_guess(n):
    num = randint(1, n)

    guess = 0
    while guess != num:

        try:    # try to verify if the entered  value is an integer.
            guess = int(input('Enter a number between 1 and {}: '.format(n)))

        except ValueError:  # if not an integer, print the following statement and terminate the program.
            print('Sorry, {} is not an integer.'.format(guess))
            exit(1)

        if guess < num:
            print('Too low! Please try again.')
        elif guess > num:
            print('Too high! Please try again.')

    print('Hurray! You have guessed the number {:02d} correctly!'.format(num))

    # open a text file and save the user input in the text file.
    try:
        txt_file = open('data.txt', 'w')
        print('Your guess: ', guess, file=txt_file)

    except FileExistsError:
        print('File "data.txt" already exists')
    except FileNotFoundError:
        print('"data.txt" not found')
    finally:
        txt_file = open('data.txt', 'r')    # open file for reading
        txt_file.close()    # close once done


your_guess(50)