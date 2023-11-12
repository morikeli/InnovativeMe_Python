from datetime import datetime

current_date = datetime.today()

def create_data_log():
    # open a text file and save the user input in the text file.
    try:
        current_time = current_date.strftime('%a %d-%m-%Y %H:%M:%S')
        txt_file = open('data.txt', 'w')
        print(f'Successful login at {current_time}', file=txt_file)
    
    except FileNotFoundError:
        print('File may have been moved to another directory or deleted.')
    
    except FileExistsError:
        print('File with the same name already exists.')
    
    finally:
        txt_file = open('data.txt', 'r')
        txt_file.close()
    
    