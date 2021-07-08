file_name = 'logs2_avg_times.txt'

def log_ids_over_1000ms(file_name):
    """[Problem] Print the average event time based on event start and finish information. 

    Args:
        file_name (.txt): This function operates under the assumption that the file containing the logs has a standard format and events will always have the same information in the same order. It will read the file line by line and gather the event start and finish information, performed a DateTime operation to calculate the total event time. It will return the average event time for all events. 
    """
    try:

        events = {
        }

        with open(file_name, 'r') as logs:
            lines = logs.readlines()
            
            for line in lines:
                fields = line.split(' ')
                if line.__contains__('Started'):
                    events[fields[2]] = [fields[0]]                 
                elif line.__contains__('Finished'):
                    events[fields[2]].append(fields[0])
            print(events)
                            
    except FileNotFoundError as err:
        print(err)
    
    except KeyError as err2:
        print(f'No event {err2} started information')

log_ids_over_1000ms(file_name)