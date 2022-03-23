# Program to display the divisors of a number.
n = int(input('Enter a number: '))
print('Divisors of {:,d} are: '.format(n), end='')
for i in range(1, n+1):
    if n%i == 0:
        print(i, ', ', sep='', end='')  # All divisors are displayed and separated by a comma. The end functions
        # prevents the print function from advancing to the next line, therefore all divisors are printed in one line.
print('\b\b')   # Deletes the comma and space, respectively, that comes after the last divisor.
