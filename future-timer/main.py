""" 
    QUIZ:
    Write a program that asks the user how many hours he/she wants to go into the future.
    The program asks the user for an hour between 1 and 12 and asks them to enter time in am or pm.
    The program also asks the user how many hours into the future they want to go.

    Program written by: Mori Keli
    Date: 06/02/2021
    ALL RIGHTS RESERVED.
"""

from message import messages


def dive_into_the_future(time, time_format, future):
    
    if ((time + future_time) == 12) and (time_format == 1):
        print(f'Time: {time} a.m. \nTime into the future: {(time + future_time)} p.m.')
    
    elif ((time + future_time) == 12) and (time_format == 2):
        print(f'Time: {time} p.m. \nTime into the future: {(time + future_time)} a.m.')
    
    elif ((time + future_time) >= 12) and (time_format == 1):
        print(f'Time: {time} a.m. \nTime into the future: {(time + future_time) - 12} p.m.')
    
    elif ((time + future_time) >= 12) and (time_format == 2):
        print(f'Time: {time} a.m. \nTime into the future: {(time + future_time) - 12} a.m.')

    else:
        _format = ['a.m.', 'p.m.']
        # use ternary operator {_format[0] if time_format == 1 else _format[1]} to index items in the list. If the
        # time_format is 1, use _format[0] to print 'a.m.' else use _format[1] to display 'p.m.'
        print(f'Time: {time} {_format[0] if time_format == 1 else _format[1]} \nTime into the future: {(time + future_time)} {_format[0] if time_format == 1 else _format[1]}')



if __name__ == '__main__':
    time_input = int(input('Enter an hour between 1 and 12: '))

    if time_input < 1 or time_input > 12:
        text_str = 'ERROR!!! This program only supports 12-hour clock system. Please try again.'
        messages.error_message(text_str)
    
    else:
        text_str = f"""
            Choose a time format. Enter '1' or '2':
            1. a.m.
            2. p.m.
        """
        messages.prompt_message(text_str)
        time_format = int(input('Enter time format: '))
        
        if (time_format < 1) or (time_format > 2):  # check if time_format input is valid
            text_str = "INVALID CHOICE! For time in 'a.m.' enter 1, for time in 'p.m.' enter 2."
            messages.error_message(text_str)
        
        else:
            future_time = int(input('How many hours do you want to go into the future: '))
            dive_into_the_future(time_input, time_format, future_time)