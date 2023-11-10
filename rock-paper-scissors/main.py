"""
    This is a rock, paper, scissors game script.
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created 11/03/2022 06:19 EAT
"""
from gameplay.game import gameplay


def validate_user_input(start_game, game_modes=['r', 's', 'p']):
    # game_modes = ['r', 's', 'p']
    
    if len(user_input) > 1:
        print('INVALID INPUT!')
    elif user_input not in game_modes:
        print('INVALID GAME MODE!')
    elif user_input.isspace() or user_input.isdigit() or user_input.isnumeric():
        print('INVALID INPUT!')
    
    return

if __name__ == '__main__':
    user_input = str(input('Enter your choice, "r" for rock, "p" for paper or "s" for scissors: ')).lower()    # convert to lowercase.
    
    validate_user_input(gameplay(user_choice=user_input))
