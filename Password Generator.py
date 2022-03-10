# program to generate a password with 16 characters selected randomly.
from random import sample

small_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = small_letters.upper()
numbers = '1234567890'
symbols = '!@$%&*'

all_char = small_letters+capital_letters+numbers+symbols
length = 16
password = "".join(sample(all_char, length))
print('Generated password: ', password)
