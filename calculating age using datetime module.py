from datetime import datetime

print('***'*25)
print('{:^70s}'.format('AGE CALCULATING PROGRAM'))
print('***'*25)
print('{:^80s}'.format('Use space as a separator, e.g. date of birth 2000 01 31'))
print('---'*25)
dob = input('Enter your date of birth(yyyy/mm/dd): ')
dob1 = datetime.strptime(dob, '%Y %m %d')   # time specifier to perform calculation.
c_date = datetime.now()  # stores the current date and time.
age = c_date - dob1  # Formula: current date - dateofbirth1(dob1)
print('---'*25)
print('{:^80s}'.format('Age: {:02d} years old'.format(int(age.days/365.25))))   # age is displayed.
print('---'*25)
print('***'*25)
