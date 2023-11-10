from .winner import winner
from random import choice

def gameplay(user_choice):
    game_mode = ['r', 's', 'p']

    computer_choice = choice(game_mode)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif winner(user_choice, computer_choice):
        print(f'You won!\nComputer\'s choice: {computer_choice}\nYour choice: {user_choice}')

    else:
        print(f'You lost!\nComputer\'s choice:{computer_choice}\nYour choice: {user_choice}')


