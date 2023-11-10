# program to check whether the number of opening brackets is the same as the closing brackets.

def math_expression(expression):
    """ This is a function to enter a mathematical expression, perform calculations and generate an answer for the calculation. """
    # iterate through the user_input string to determine the length of string
    for chars in expression:
        open_b = expression.count('(')  # count the number of opening brackets
        close_b = expression.count(')')     # count the number of closing brackets

        if open_b < close_b or close_b < open_b:    # check for missing brackets
            print('Syntax Error: Missing Bracket\n'+expression)
            print(' '*len(expression)+'^')  # multiply spaces with the no. of characters in the string to position the caret where the closing bracket needs to be added.
            break

        else:   # if there is no syntax error, evaluate the expression -> perform addition, subtraction, multiplication, division
            evaluate_expression = eval(expression)
            print(f'Result: {evaluate_expression}')
            break
    
    return

if __name__ == '__main__':
    user_expr = str(input('Type your expression or formula (brackets should be included): '))
    math_expression(user_expr)