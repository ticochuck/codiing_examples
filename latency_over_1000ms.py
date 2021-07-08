file_name = 'logs1.txt'

def log_ids_over_1000ms(file_name):
    try:
        with open(file_name, 'r') as logs:
            lines = logs.readlines()
            
            for line in lines:
                words = line.split(' ')
                if int((words[-1][:-3])) > 1000:
                    print(*words[:2])

    except FileNotFoundError as err:
        print(err)

log_ids_over_1000ms(file_name)