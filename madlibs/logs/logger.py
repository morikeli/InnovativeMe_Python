
def create_data_logs(data):
    try:
        txt_file = open('data.txt', 'a')
        print(data, file=txt_file)

    except FileNotFoundError:
        print('File not found')
    
    except FileExistsError:
        print('File with the same name already exists.')
    
    finally:
        txt_file = open('data.txt', 'r')
        txt_file.close()
