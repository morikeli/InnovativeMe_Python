def create_log_file(data):
    try:
        with open('data.txt', 'a+') as file:
            file.write(data)
    
    except FileNotFoundError:
        return 'Log file not found!'
    
    except FileExistsError:
        return 'A log file with the same name already exists!'