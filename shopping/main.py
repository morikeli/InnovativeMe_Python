import sys
from datetime import datetime as dt

print('==='*30)
print(f"{'YOUR SHOPPING PROGRAM':^80s}")
print('---'*30)
print(f"Current date: {dt.now().strftime('%d-%b-%Y %H:%M:%S'):>68s}")
print('==='*30)
print(f"{'>--->-->-> Type "exit" to terminate the program! <-<--<---<':^79s}")
print(f"{'---'*15:^79s}")

item = 0
itemList = []
priceList = []
count_item = 0

while item != 'exit':
    count_item += 1
    item = str(input('Enter an item: '))
    
    if item == 'exit':
        continue
    else:
        price = float(input('Enter the price of the item: '))

    itemList.append(item)
    priceList.append(price)

else:
    print('===' * 30)
    print('{} {:>70s}'.format('Item(s)', 'Price'))
    for items, price in zip(itemList, priceList):
        print('{}:{:>75,.2f}'.format(items.capitalize(), price))

    print('---'*30)
    print('No. of items: {:>63,d}'.format(count_item - 1))   # minus 1 to reduce the no. of iteration since command 'exit' is not an item.
    print('Total Cost: {:>70,.2f}'.format(sum([price for price in priceList])))
    print('---'*30)
    print('{:^70s}'.format('*** END OF PROGRAM! ***'))
    print('==='*30)


sys.exit()