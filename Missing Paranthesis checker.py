# program to check whether the number of opening brackets is the same as the closing brackets.
user_input = str(input('Type your formula (brackets should be included): '))

# iterate through the user_input string to determine the length of string
for chars in user_input:
    open_b = user_input.count('(')  # count the number of opening brackets
    close_b = user_input.count(')')     # count the number of closing brackets

    if open_b < close_b or close_b < open_b:
        print('Syntax Error: Missing Bracket\n'+user_input)
        print(' '*len(user_input)+'^')  # multiply spaces with the no. of characters in the string to position the caret where the closing bracket is null
        break
    else:
        # if user_input.isalnum():
        #     alphabet = 'abcdefghijklmnopqrstuvwxyz'
        #     # if user_input in alphabet:
        #     for char in user_input.lower():
        #         x = len(user_input)
        #
        #         loc_char = user_input.index(str(alphabet))
        #         print(' '*int(loc_char)+'^')
        # else:
        add_user_input = eval(user_input)
        print('Result: {}'.format(add_user_input))
        break
print('End of program!')
