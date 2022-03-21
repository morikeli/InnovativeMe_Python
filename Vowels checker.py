# Program to determine if a string contains vowels

s = str(input('Type your text... '))
for i in range(len(s)):
    if ('a' or 'e' or 'i' or 'u') in s:
        s_true = True

        # Save data int the text file before printing it
        txt_file = open('C:/Users/Documents/Coding/Python/Program to determine vowels in a string/data.txt', 'w')
        print(s_true, file=txt_file)

        print(s_true)
        break
    else:
        s_false = False

        txt_file = open('C:/Users/Documents/Coding/Python/Program to determine vowels in a string/data.txt', 'w')
        print(s_false, file=txt_file)

        print(s_false)
        break
