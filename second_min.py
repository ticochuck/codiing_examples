# find the second minimun value in an unsorted array
import sys 

arr = [8,6]

def find_second_min(arr):
    
    min_val = sys.maxsize
    second_min_val = sys.maxsize
    for x in arr:
        if x < min_val:
            second_min_val = min_val
            min_val = x
        elif x > min_val and x < second_min_val:
            second_min_val = x

    # print(f'Second minimun in {arr} = {second_min_val}')
    return second_min_val

find_second_min(arr)