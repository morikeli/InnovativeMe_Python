a = []
for i in range(10):
    txt = str(input('Enter an item: '))
    a.append(txt)
a.sort()
print(a)
print('New List: \n\b', a)
print('The largest item in the list is: ', a[-1])

