"""
    2022 | ALL RIGHTS RESERVED.
    Program developed, debugged and maintained by Mori Keli.
    Created: 04/04/2022 10:46 EAT

    Updates:
    --------------
    * Accept user input
    * print x in a text file.
    * change the whole string into lowercase.
    * if derivative is 0, e.g. x^1 returns 1x.
    * text file will contain a history of x input by the user and their respective result.

"""
# Program to print the derivative of a given expression
x = str(input('Enter an expression to find the derivative, e.g.(x^4): '))
if '^' not in x:
    print('Invalid expression.')
    exit(1)
else:
    for c in x.lower():
        caret_index = x.index('^')  # find the position of '^' using index method
        derivative = int(x[caret_index+1:])-1   # position of the index, add 1 to access items after the caret.
        if derivative == 0:
            print(f'Derivative: {x[caret_index+1:]}x')
        else:
            print(f'Derivative: {x[caret_index+1:]}x^{derivative}')

        #  print result in a text file before breaking the loop.
        txt_file = open('data.txt', 'a')
        if derivative == 0:
            print(f'Derivative of {x}: {x[caret_index+1:]}x', file=txt_file)
        else:
            print(f'Derivative of {x} is {x[caret_index+1:]}x^{derivative}.', file=txt_file)
        txt_file.close()

        break   # terminate the loop to prevent derivative from being printed a no. of times(depending on the length of x).
