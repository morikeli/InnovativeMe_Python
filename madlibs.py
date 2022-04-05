"""
    2022 ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created 4/4/2022 1857 EAT
"""

# Simple Mad Libs program
def get_input(user_input, adjective, activity):
    print('---'*30)
    if (user_input or adjective or activity).isdigit():
        if (user_input or adjective or activity).isnumeric():
            return f'Invalid input. Input cannot contain a number or digits.\nCollege: {user_input}\nAdjective: {adjective}\nActivity: {activity}'
    else:
        # Print story in a text file before displaying in terminal.
        try:
            txt_file = open('data.txt', 'a')
            x = f'{user_input} class was a really {adjective} class today. We learned how to {activity} today in class. I can\'t wait for ' \
                f'tomorrow\'s ' \
                f'class!'
            print(x, file=txt_file)
        except FileNotFoundError:
            print('File not found')
        except FileExistsError:
            print('File with the same name already exists.')
        finally:
            txt_file = open('data.txt', 'r')
            txt_file.close()

        return f'{user_input} class was a really {adjective} class today. We learned how to {activity} today in class. I can\'t wait for tomorrow\'s ' \
               f'class!'


print(get_input(user_input=str(input('Enter a college: ')), adjective=str(input('Enter an adjective: ')), activity=str(input('Enter an activity: '))))
