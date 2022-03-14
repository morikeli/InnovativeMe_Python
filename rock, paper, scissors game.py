"""
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created 11/03/2022 06:19 EAT
"""
# Rock, paper, scissors game

from random import choice


def gameplay():
    game_mode = ['r', 's', 'p']
    user_choice = str(input('Enter your choice, "r" for rock, "p" for paper or "s" for scissors: ')).lower()    # convert to lowercase.

    computer_choice = choice(game_mode)

    if user_choice is computer_choice:
        return 'It\'s a tie!'

    elif winner(user_choice, computer_choice):
        return 'You won!\nComputer\'s choice: {}\nYour choice: {}'.format(computer_choice, user_choice)

    return 'You lost!\nComputer\'s choice:{}\nYour choice: {}'.format(computer_choice, user_choice)


def winner(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True

# gameplay()    # calling a function without the print statements does not display the return statements


print(gameplay())
