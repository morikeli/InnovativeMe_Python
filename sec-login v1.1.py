"""
    2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged and maintained by Mori Keli.
    Created: 16/03/2022 0707hrs EAT
"""
# Updated Secure login program(v1.1)
# The program increment login time if the user enters incorrect password.

from datetime import datetime
from time import sleep

password = '12345'

n = 0
i = 0
current_date = datetime.today()
current_min = current_date.minute
current_sec = current_date.second
x = current_min

print('***'*30)
print('{:^75s}\n{}'.format('Secure Login', '---'*30))
print('Current date: {:>75s}'.format(current_date.strftime('%a %dth-%b-%Y %H:%M:%S')))
print('***'*30)

while i == 0:

    def timer():
        global n, x
        n += 2
        x += n
        print('!!!'*30)
        print('Incorrect Password! \nNext login: {:2}:{:02d}:{:02d}\nDuration: {} minutes'.format(current_date.strftime('%H'), x, current_sec, n))
        print('Loading ...')
        print('!!!'*30)
        print('---'*30)
        sleep(n*60)     # delay program execution for n*60 seconds


    user_password = str(input('Enter your password: '))

    if user_password == password:
        print('Successful login')
        exit(0)  # terminate the program

        # continue
            # exit(0)
    else:
        timer()  # call function 'timer'


