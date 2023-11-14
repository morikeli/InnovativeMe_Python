"""
    This script is inspired by an episode I watched in the "Salvation" TV series where a whistleblower tried to access a government institutional system to make confidential info. public because the general public was not aware of the impending danger that could be the end of the world.
    Everytime he entered an incorrect password the system will delay the next login prompt.

    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged and maintained by Mori Keli.
    Created: 16/03/2022 0707HRS EAT

    Your feedback is highly appreciated.
"""
# This is a script to allow a user to login into a system (applicable in desktop app or mobile app). The script delays a login prompt if the user enters an incorrect password.
# The program increments login time if the user enters incorrect password.

from datetime import datetime
from time import sleep

PASSWORD = '12345'  # In this case the password will be a constant for testing purpose.


current_date = datetime.today()
current_min = current_date.minute
current_sec = current_date.second


print('***'*30)
print(f'{"Secure Login":^75s}\n{"---"*30}')
print('Current date: {:>75s}'.format(current_date.strftime('%a %dth-%b-%Y %H:%M:%S')))
print('***'*30)


def user_login_prompt(delay=0):
    while True:
        current_min = current_date.minute   # get current minute from latest login attempt.
        delay += 2
        current_min += delay    # add delay to the current minute
        print('!!!'*30)
        print(f'Incorrect Password! \nNext login: {current_date.strftime("%H"):2}:{current_min:02d}:{current_sec:02d}\nDuration: {delay} minutes')
        print('Loading ...')
        print('!!!'*30)
        print('---'*30)
        sleep(delay*60)     # delay program execution for n*60 seconds

        user_password = str(input('Enter your password: '))

        # if login is successful, print "Logged in" else call the function.
        return 'Logged in!' if user_password == PASSWORD else user_login_prompt()



if __name__ == '__main__':
    user_password = str(input('Enter your password: '))


    if user_password == PASSWORD:
        print('Successful login')
        exit(0)  # terminate the program
        
    else:
        prompt = user_login_prompt()
        print(prompt)