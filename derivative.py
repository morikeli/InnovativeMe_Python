"""
    2022 | ALL RIGHTS RESERVED.
    Program developed, debugged and maintained by Mori Keli.
    Created: 04/04/2022 10:46 EAT
"""
# Program to print the derivative of a given expression
x = 'x^2'

for c in x:
    caret_index = x.index('^')  # find the position of '^' using index method
    derivative = int(x[caret_index+1:])-1   # position of the index, add 1 to access items after the caret.
    print(f'{x[caret_index+1:]}x^{derivative}')
    break   # terminate the loop to prevent derivative from being printed a no. of times(depending on the length of x).
