"""
    2022 ALL RIGHTS RESERVED.
    Program developed. maintained and debugged by Mori Keli.
    Created 05/04/2022 0630 EAT
"""


def derivative(x):
    if '^' not in x:
        print('Invalid expression.')
        exit(1)
    else:
        for c in x.lower():
            caret_index = x.index('^')  # find the position of '^' using index method
            derivative = int(x[caret_index+1:])-1   # position of the index, add 1 to access items after the caret.
            if derivative == 0:
                return f'Derivative: {x[caret_index+1:]}x'
            else:
                #  print result in a text file before breaking the loop.
                try:
                    txt_file = open('data.txt', 'a')
                    if derivative == 0:
                        print(f'Derivative of {x}: {x[caret_index+1:]}x', file=txt_file)
                    else:
                        print(f'Derivative of {x} is {x[caret_index+1:]}x^{derivative}.', file=txt_file)
                        txt_file.close()
                except FileNotFoundError:
                    return 'text file not found'
            return f'Derivative: {x[caret_index + 1:]}x^{derivative}'


print(derivative(x=str(input('Enter an expression to find the derivative, e.g.(x^4): '))))
