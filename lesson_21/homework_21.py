import logging
import time
from pathlib import Path

def select_log_by_key(path:Path, key:str):

    with open(path, 'r') as log:
        content = log.readlines()

    selected_log = [x for x in content if x.__contains__(key)]

    return selected_log

def analysis_and_logging(log_selected:list, filename):
    time_temp = []
    time_format = "%H:%M:%S"

    start_index = log_selected[0].find('Timestamp ') + 10
    end_index = start_index + 8

    for s in range(len(log_selected)):
        time_str = log_selected[s][start_index:end_index]
        time_obj = time.strptime(time_str, time_format)
        time_temp.append(time_obj)

        if s > 0 and s < len(log_selected):
            time_difference = time_temp[s][5] - time_temp[s-1][5]
            if abs(time_difference) in range(31,34):
                logging.basicConfig(level=logging.WARNING, filename=filename, filemode="w+")
                logging.warning(
                    f'current log item: {log_selected[s]} previous log item: {log_selected[s - 1]} difference: {abs(time_difference)} sec')

            elif abs(time_difference) > 33:
                logging.basicConfig(level=logging.ERROR, filename=filename, filemode="w+")
                logging.error(
                    f'current log item: {log_selected[s]}previous log item:  {log_selected[s - 1]}difference too much: {abs(time_difference)} sec')

    return open(filename, mode='r')



log_file_full = Path('hblog.txt')
key = 'Key TSTFEED0300|7E3E|0400'
log_file_selected = 'hb_test.log'

list_selected_items = select_log_by_key(log_file_full, key)

file_to_read = analysis_and_logging(list_selected_items, log_file_selected)

print(file_to_read.read())
