"""
    © 2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created: 04-03-2022 0828hrs EAT
"""

from time import sleep
from datetime import datetime

user_password = '1234'
pin = ''

current_date = datetime.today()    # get current date & time
current_min = current_date.minute   # store current minute
current_sec = current_date.second   # store current second

if pin != user_password:
    print('You will see the login prompt after {} minutes i.e {}:{:02d}:{:02d}'.format(2, current_date.strftime('%H'), current_min+2, current_date.second))
    sleep(120)    # delays login prompt for 120 seconds.

    print('{}:{:02d}:{:02d}'.format(current_date.strftime('%H'), current_min+2, current_sec))
    user_input = str(input('Enter password: '))
    if user_password != user_input:
        print('Incorrect Password!')
        for i in range(4):
            user_input = str(input('Enter password: '))
            if i == 3 and user_input != user_password:
                print('Account blocked!')

                try:    # try opening a text file and print status 'Account blocked' in it.
                    txt_file = open('data.txt', 'w')
                    print('Account blocked!', file=txt_file)
                    txt_file.close()

                except FileNotFoundError:
                    print('"data.txt" may have been deleted or moved to another location.')
                except FileExistsError:
                    print('File with the same name already exists.')
                finally:
                    txt_file = open('data.txt', 'r')
                    txt_file.close()

                exit()  # terminate the program after writing data into txt_file
            else:
                print('Successful login.')
                exit()  # acts as a break statement.

    else:
        print('Successful login.')

        try:  # try opening a text file and print status 'Account blocked' in it.
            txt_file = open('data.txt', 'w')
            print('Successful login at {}'.format(current_date.strftime('%a %d-%m-%Y %H:%M:%S')), file=txt_file)
            txt_file.close()

        except FileNotFoundError:
            print('"data.txt" may have been deleted or moved to another location.')
        except FileExistsError:
            print('File with the same name already exists.')
        finally:
            txt_file = open('data.txt', 'r')
            txt_file.close()

exit(0)     # terminate program once done.
