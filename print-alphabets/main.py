# This is a script to print letters of the English alphabet.
import string

# Method 1 - using unicode characters of the letters
for letter in range(ord('A'), ord('Z') + 1):
    print(chr(letter), end=', ')    # print all letters in one line

print()

# Method 2 - using string module
for letter_ in string.ascii_uppercase:
    
    print(letter_, end=', ')

print()
