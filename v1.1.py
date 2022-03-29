"""
    2022 ALL RIGHTS RESERVED.
    Program to developed, debugged and maintained by Mori Keli.
    Created 29/03/2022 1139hrs EAT
"""

# Program to print number n in words.

d = {1: 'one', 2: 'two', 100: 'hundred', 20: 'twenty'}
n = 122
x = str(n)

if len(str(n)) == 3:
    print(f'Number: {n}')
    print(f'{str(d[int(x[0])])} {d[100]} and {d[20]} {d[int(x[1])]}')
