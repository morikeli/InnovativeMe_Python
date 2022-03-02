# Write a program that tells the user the no of pennies, dimes, nickels and quarters in a dollar.
price = int(input('Enter the purchase price of the item: '))


change = 100 - price

print('==='*25)
# no. of pennies in the change
pe_n = change/1
print('There are {:.2f} pennies in {:3d}'.format(pe_n, change))

# no. of dimes in the change
dimes = change/5
print('There are', dimes, 'dimes in', change, 'cents')

# no. of nickels in the change
nickels = change/10
print('There are', nickels, 'nickels in', change, 'cents')

# no. of quarters in the change
quarters = change/25
print('There are', quarters, 'quarters in', change, 'cents')

print("==="*25)

print('Returned change: ${:.2f}'.format(change/100))
print('Returned change(in cents): ', change, '¢')
