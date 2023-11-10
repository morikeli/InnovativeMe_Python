# program to generate a password with 30 characters selected randomly.
from string import ascii_lowercase, ascii_uppercase, digits
from random import sample

LOWERCASE_LETTERS = ascii_lowercase
UPPERCASE_LETTERS = ascii_uppercase
DIGITS = digits
SPECIAL_CHARS = '!@#$%^&*_+'


def generate_password(length=30):
    join_chars = LOWERCASE_LETTERS + UPPERCASE_LETTERS + DIGITS + SPECIAL_CHARS
    password = ''.join(sample(join_chars, length))

    print(f'Generated password: {password}')
    return

if __name__ == '__main__':
    generate_password()
    