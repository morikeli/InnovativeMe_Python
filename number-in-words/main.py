"""
    This is a Python script that displays the name of a given number.

    2022 MORI KELI | ALL RIGHTS RESERVED.
    Program developed, debugged, tested and maintained by Mori Keli.
    Created: 29/03/2022 2035hrs EAT

"""
from number_examples.numbers import numbers_dict


def number_in_words(number, _word=''):
    """ 
        This is a function that prints out a number in its word equivalent.
        For example,
            1 is one,
            2 is two,
            3 is three
            100 is hundred
            250 is two hundred and fifty
            375 is three hundred and seventy five
            1000 is thousand
    """
    
    if int(number) in numbers_dict:    # check if the number exists in numbers_dict
        _word = str(numbers_dict[int(number)]).capitalize()
    
    else:   # if the number does not exist in numbers-dict
        # Most numbers not available in numbers_dict are 2-digit numbers or more.
        # To generate words for such numbers, we must use their place values and total values, e.g.
        # 25 - has two digits. The place value of 5 is 'ones', the place value of 2 is 'tens'
        # 125 - has 3 digits. The place value of 5 is 'ones', 2 is 'tens', 1 is hundreds
        # 1250 - has 4 digits. The place values of 1, 2, 5, 0 is 'thousands', 'hundreds', 'tens', and 'ones' respectively.
        
        if len(number) == 2: # range 21 - 99 exluding numbers in numbers_dict, e.g. 30, 40, 50, etc.

            # total value for a digit at index 1 in number, e.g. 
            # the total value of '2' in 125 is 20 (i.e. 2 x 10), of '1' is 100 (i.e. 1 x 100)
            tens = int(number[0]) * 10    
            
            _word = f"{str(numbers_dict[tens])} {numbers_dict[int(number[1])]}"

        elif len(number) == 3:  # range 100 - 1,000
            ones = int(number[2])
            tens = int(number[1]) * 10
            
            if number[1:] == '00':
                _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[100])}"
            
            else:
                if tens == 0:
                    _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[100])} and {str(numbers_dict[ones])}"
                
                else:
                    _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[100])} and {str(numbers_dict[tens])} {str(numbers_dict[ones])}"

        elif len(number) == 4:  # range 1,000 - 9,999
            ones = int(number[3])
            tens = int(number[2]) * 10
            hundreds = int(number[1])
            
            if number[2:] == '00':
                _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[1000])} {str(numbers_dict[hundreds])} {str(numbers_dict[100])}"
            
            else:
                # there are numbers where the place value of 'hundreds' or 'tens' or 'ones' is 0.
                # For example, 2003, 1010, 2020, 2022, 2105 , 
                if hundreds == 0:   # check for numbers with digits 0 at the hundreds place value.
                    if (number[-1] == '0'):     # check if the place value of 'ones' is 0
                        _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[1000])} and {str(numbers_dict[tens])}"

                    elif number[-2] == '0':   # check if place value of 'tens' is 0
                        _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[1000])} and {str(numbers_dict[int(number[-1])])}"

                    else:
                        if int(number[2:]) in numbers_dict:
                            _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[1000])} and {str(numbers_dict[int(number[2:])])}"
                            
                        else:    
                            _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[1000])} and -- {str(numbers_dict[tens])}"
                else:
                    if tens == 0:
                        _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[1000])}, {str(numbers_dict[hundreds])} {str(numbers_dict[100])} and {str(numbers_dict[ones])}"
                    else:
                        _word = f"{str(numbers_dict[int(number[0])])} {str(numbers_dict[1000])}, {str(numbers_dict[hundreds])} {str(numbers_dict[100])} and {str(numbers_dict[tens])} {str(numbers_dict[ones])}"

        
        else:
            pass
    
    return str(_word).capitalize()


if __name__ == '__main__':
    number_input = int(input('Enter a number: '))
    
    if number_input < 0:    # check for negative numbers
        absolute_number = abs(number_input)   # remove the negative sign
        result = number_in_words(str(number_input))    # convert the number to a string 
        print(f'Number: {number_input} \nNumber in words: {result}')
    
    else:
        result = number_in_words(str(number_input))    # convert the number to a string
        print(f'Number: {number_input} \nNumber in words: {result}')
