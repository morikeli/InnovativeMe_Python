# Program to replace every character in a string with an asterisk
# I plan to use the following concept to clone a login system.

mystring = str(input('Enter a string: '))
for i in mystring:
    mystring += i
    x = mystring.replace(mystring, '*')
    print(x, end='')    # end function eliminates a new line

