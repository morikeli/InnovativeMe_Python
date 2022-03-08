# cipher program
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'qwertyuiopzxvbncmasdfghjkl'

message = input('Enter your message: ')

for chars in message.lower():
    if chars.isalpha():
        print(key[alphabet.index(chars)], end='')
    else:
        print(chars, end='')
