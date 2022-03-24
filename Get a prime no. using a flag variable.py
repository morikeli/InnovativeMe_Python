# Program to determine whether a number is prime or not using a flag variable.
from datetime import datetime
d = datetime.now()


def program_display():
    print('==='*30)
    print('{:^85s}'.format('--- PROGRAM TO DETERMINE IF A NUMBER IS PRIME OR NOT ---'))
    print('==='*30)
    print('{:>70s}{}'.format('Last Run: ', d.strftime("%d-%m-%Y %H:%M:%S")))
    print('---'*30)


program_display()


def prime_number(num):
    if num == 1:
        print('1 is not a prime number.')
        exit(0)
    elif num < 0:
        print('INVALID INPUT!!! Please enter a positive integer.')
        exit(1)

    flag = 0
    divisors_list = []
    for i in range(2, num):
        if num % i == 0:
            flag = 1

    # for loop to iterate through divisors of the given number.
    for j in range(1, num+1):
        if num % j == 0:
            divisors_list.append(j)

    if flag == 1:
        print('{} is not a prime number.'.format(num), end='')
        print('This is because {} has more than two divisors.\nDivisors of {} are: {}'.format(num, num, divisors_list))
    else:
        print('{} is a prime number.'.format(num), end=' ')
        print('This is because {} is only divisible by {} and {}.'.format(num, divisors_list[0], divisors_list[1]))

    try:
        data_file = open('data.txt', 'w')
        print('File created: {}'.format(d.strftime("%d-%m-%Y %H:%M:%S")), file=data_file)
        print('{:,d} is a prime number.'.format(num), file=data_file)
    except FileExistsError:
        pass
    except FileNotFoundError:
        print('"data.txt" may have been deleted or moved to another location')
    finally:
        data_file = open('data.txt', 'w')
        data_file.close()


prime_number(int(input('Enter a number: ')))
