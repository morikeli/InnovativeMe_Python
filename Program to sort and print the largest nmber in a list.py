a = []
n = int(input('How many items do you want to append into your list: '))
for i in range(1, n+1):
    b = input('Enter the items: ')
    if b.isdigit():
        a.append(b)
    else:
        print('Error!!! Only integers are appended into the list.')
        exit(1)
a.sort()
print(a)
print('The largest number in the list is ', a[-1])
