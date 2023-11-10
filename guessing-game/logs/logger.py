def create_data_log(data):
    # open a text file and save the user input in the text file.
    try:
        txt_file = open('data.txt', 'w')
        print('Your guess: ', data, file=txt_file)

    except FileExistsError:
        print('File "data.txt" already exists')
    except FileNotFoundError:
        print('"data.txt" not found')
    finally:
        txt_file = open('data.txt', 'r')    # open file for reading
        txt_file.close()    # close once done
