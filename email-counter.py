# program to check prof email addresses and student email addresses.
user_input = int(input('How many email addresses are you entering? '))
email_type = ''
email_count_stud = ''
email_count_prof = ''

for i in range(user_input):
    emails = str(input('Enter the email addresses: '))
    email_type = emails[emails.index('@'):]
    email_count_stud = email_type.count('student')
    email_count_prof = email_type.count('prof')

if 'student' in email_type:
    print('All email addresses provided are student emails.')
else:
    print('{} professor email addresses found'.format(email_count_prof))
try:
    txt_file = open('data.txt', 'w')
    print(user_input, file=txt_file)
except FileExistsError:
    print('File exists!')
except FileNotFoundError:
    print('File not found!')
finally:
    txt_file = open('data.txt', 'r')
    txt_file.close()
