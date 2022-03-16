num = int(input('Enter an integer: '))
digit = str(num)
answer = 0
for i in range(len(digit)):
    answer += int(digit[i])
print('Sum of the digits of {:,d} = {:,d}'.format(num, answer))
