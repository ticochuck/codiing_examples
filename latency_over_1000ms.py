file_name = 'logs1.txt'

def log_ids_over_1000ms(file_name):
    """[Problem] Print all the Error IDs for events with latency over 1000ms

    Args:
        file_name (.txt): This function operates under the assumption that the file containing the logs has a standard format and events will always have the same information in the same order. It will read the file line by line and convert the ms string to an integer. It will print the event IDs where the latency is greater than 1000ms. 
    """
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