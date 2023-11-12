"""
    2022 ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created 4/4/2022 1857 EAT
"""

from logs.logger import create_data_logs

# Simple Mad Libs program
def get_user_input(user_input, adjective, activity):
    print('---'*30)

    text_str = f"{user_input} class was a really {adjective} class today. We learned how to {activity} today in class. I can\'t wait for tomorrow\'s class!"

    if (user_input or adjective or activity).isdigit():
        if (user_input or adjective or activity).isnumeric():
            return f'Invalid input. Input cannot contain a number or digits.\nCollege: {user_input}\nAdjective: {adjective}\nActivity: {activity}'
    
    else:
        # Print story in a text file before displaying in terminal.
        create_data_logs(text_str)

        return text_str

if __name__ == '__main__':
    text:str = input('Enter a college: ')
    text_adjective:str = input('Enter an adjective: ')
    text_activity:str = input('Enter an activity: ')


    result = get_user_input(user_input=text, adjective=text_adjective, activity=text_activity)
    print(result)
    