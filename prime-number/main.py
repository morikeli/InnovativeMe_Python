# Python script to print the first 100 numbers
num_range = range(1, 101)

def is_prime(number):
    """ This is a function to check if a number is a prime number. """

    for n in range(2, number):
        if number % n == 0:
            return False
    
    return True  # if n is a prime number, return True.


if __name__ == '__main__':
    prime_nums = list(filter(is_prime, num_range))
    print(prime_nums)