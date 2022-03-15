"""
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, maintained by Mori Keli.
    Created Thur 03-03-2021 21:06
"""

# Program to emulate sim-card pin login.
# The account or phone number is blocked after 4 failed attempts.
from datetime import datetime
i = 0
countdown_tries = 4
user_pin = '1234'
current_date = datetime.today()
while True:
    i += 1
    countdown_tries -= 1
    user_input = str(input('Enter pin: '))

    if user_input != user_pin:
        if user_input != user_pin and i == 4:
            print('Account blocked!')
            # break
            exit(-1)  # terminate the program if 4 tries were all unsuccessful. A break keyword can also be used.
        else:
            if countdown_tries == 1:
                print('Invalid pin. You have {:02d} attempt left.'.format(countdown_tries))  # print attempt in singular form if countdown_tries is equal
                # to 1
            else:
                print('Invalid Pin. You have {:02d} attempts left.'.format(countdown_tries))

    else:
        print('Successful login.')

        try:
            current_time = current_date.strftime('%a %d-%m-%Y %H:%M:%S')
            txt_file = open('data.txt', 'w')
            print('Successful login at {}'.format(current_time), file=txt_file)
        except FileNotFoundError:
            print('File may have been moved to another directory or deleted.')
        except FileExistsError:
            print('File with the same name already exists.')
        finally:
            txt_file = open('data.txt', 'r')
            txt_file.close()

        exit(0)  # terminate the program after a successful login
