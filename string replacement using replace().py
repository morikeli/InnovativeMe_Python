user_string = input('Enter a string: ')
for c in range(len(user_string)):
    new_s = user_string.replace(user_string[2 - 1], '*')
    print(new_s + '!!!')  # add 3 exclamation marks at the end of the string.
    break
print('End of program!')