"""
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, maintained by Mori Keli.
    Created Thur 03-03-2021 21:06
"""

from logs.logger import create_data_log

USER_PIN = 1234   # provide a constant 4-digit pin

def sim_card_pin_prompt(user_pin, i=0, trials=4):
    """
        Program to emulate sim-card pin login prompt in mobile devices. The phone number is blocked after 4 failed attempts.

        Paramaters used:
            - user_pin is the pin entered by the user
            - i is the number of iterations
            - trials is the maximum no. of trials a user is prompted to enter his/her pin.
    """

    while True:
        i += 1
        trials -= 1

        if user_pin != USER_PIN:
            if i == 1: print('INVALID PIN!!!')
            user_input = int(input('Enter your pin: '))
            
            if user_pin != USER_PIN and i == 4:
                print('Account blocked!')
                # break
                exit(-1)  # terminate the program if 4 tries were all unsuccessful. A break keyword can also be used.
            else:
                if trials == 1:
                    print(f'Invalid pin. You have {trials:02d} attempt left.')  # print attempt in singular form if trials is equal
                    # to 1
                else:
                    print(f'Invalid Pin. You have {trials:02d} attempts left.')

        else:
            print(f'Successful login!')
            return create_data_log()  # print data in log file


if __name__ == '__main__':
    user_input = int(input('Enter your sim card pin: '))
    pin = sim_card_pin_prompt(user_input)
    
    
    