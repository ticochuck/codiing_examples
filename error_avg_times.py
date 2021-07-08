from datetime import datetime, timedelta, date, time

file_name = 'logs2_avg_times.txt'

def parser(data):
    date_info = data[0][:10]
    time_info = data[0][11:]
    formatted_dt = date_info + ' ' + time_info
    return formatted_dt


def log_ids_over_1000ms(file_name):
    """[Problem] Print the average event time based on event start and finish information. 

    Args:
        file_name (.txt): This function operates under the assumption that the file containing the logs has a standard format and events will always have the same information in the same order. It will read the file line by line and gather the event start and finish information, performed a DateTime operation to calculate the total event time. It will return the average event time for all events. 
    """
    try:

        events = {
        }
        averages = []

        with open(file_name, 'r') as logs:
            lines = logs.readlines()
            
            for line in lines:
                fields = line.split(' ')
                event_id = fields[2]
                if line.__contains__('Started'):
                    formatted_dt = parser(fields)
                    events[event_id] = [datetime.strptime(formatted_dt, "%Y-%m-%d %H:%M:%S")]                 
                elif line.__contains__('Finished'):
                    formatted_dt = parser(fields)
                    events[event_id].append(datetime.strptime(formatted_dt, "%Y-%m-%d %H:%M:%S"))
                    averages.append(events[event_id][1] - events[event_id][0])
                                
            total = averages[0]
            for x in range(1,len(averages)):
                total += averages[x]
            
            final_avg = total/len(averages)
            print(f'Event Average Duration = {final_avg}')
            return final_avg
        
    except FileNotFoundError as err:
        print(err)
    
    except KeyError as err2:
        print(f'No event {err2} started information')



log_ids_over_1000ms(file_name)