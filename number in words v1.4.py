"""
    2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged, tested and maintained by Mori Keli.
    Created: 29/03/2022 2035hrs EAT

    Updates:
    ----------
        - User input
        - Wider range of numbers
        - Better number readability
        - Capitalize functionality
        - Negative number not allowed.
    ----------
"""
# Program to print the name of an integer.
# The name of the integers are stored in a dictionary d with integers as the keys and names as the values.

d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
     20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'}

n = int(input('Enter a number: '))
if n < 0:   # Negative numbers are not allowed.
    print('Enter a positive integer.')
    exit(1)
elif n == 0:
    print('Zero')
    exit(0)     # terminates the program at this point.
x = str(n)
y = x[-2:]

print(f'Number n: {n}')
print('Number in words: ', end='')

if len(x) == 3:
    tens = int(x[1]) * 10   # total value of number n at index 1.

    if '0'*len(x[1:]) == y[-2:]:    # if string '0' multiplied by the no. of characters in x is last two characters in y, i.e zero(e.g. 300, 100, etc.).
        print('{} {}.'.format(d[int(x[0])].capitalize(), d[100]))
    else:
        if int(y) in d:
            print('{} {} and {}.'.format(d[int(x[0])].capitalize(), d[100], d[int(y)]))
        else:
            print('{} {} and {} {}.'.format(d[int(x[0])].capitalize(), d[100], d[tens], d[int(x[2])]))
else:
    y = x[:]
    tens = int(x[0])*10   # for a 2-digit number, the tens total value is at index 0.
    if (int(y) not in d) and len(str(x)) == 2:
        print('{} {}.'.format(d[tens].capitalize(), d[int(x[1])]))
    else:
        print('{}.'.format(d[n].capitalize()))     # n is length 2.
