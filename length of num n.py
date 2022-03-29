"""
    2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged and maintained by Mori Keli.
    Created 28/03/2022 1903hrs EAT
"""

# Program that determines if the length of a randomly generated number is equal to n
from random import randint
def length_num(n):
    r = randint(1, 10000)

    if len(str(r)) == n:
        print(r)    # random number
        return f'Length of random integer: {len(str(r))}'   # length of the random number.

    # else it will return None

print(length_num(n=int(input('Enter a number: '))))