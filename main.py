import time
import threading
from numpy import linspace
import playsound
import os

from database import *

ds_path = 'timer_data/records.csv'
sound_path = './alarm_sound.mp3'
save_delay = 5*60 # in seconds

def play_sound(sound_path):
    playsound.playsound(sound_path, True)

def start_timer(coldown_in_seconds ,print_per_percentage=.2):

    elapsed_time = 0

    print_time_stamps = linspace(1, coldown_in_seconds, int(1.0/print_per_percentage), dtype='int32')[1:-1].tolist()

    while (elapsed_time/coldown_in_seconds) != 1.0:
        elapsed_time += 1
        
        time.sleep(1)
        
        if round(elapsed_time) in print_time_stamps:
            print(f'{int((elapsed_time/coldown_in_seconds)*100)}% passed. ({elapsed_time}/{int(coldown_in_seconds)})')

    print('Done')

    time.sleep(.1)
    
    for _ in range(2):
        play_sound(sound_path)
    
    input('Press Enter to exit.')
    
def start_counting(date):
    year, day = date
    
    year, day, time_used, record_index = return_record_in_dataset(year, day)
    
    if record_index == -1:
        write_to_file(ds_path, f'{year}-{day}, 0\n', mode='a')
    
    year, day, time_used, record_index = return_record_in_dataset(year, day)
    
    i = 0
    while True:
        i += 1
        
        if i % save_delay == 0:
            time_used += save_delay
            
            write_to_file(ds_path, f'{year}-{day}, {time_used}\n', 
                          index=record_index)
        
        time.sleep(1)

def get_current_year_day():
    return [int(x) for x in time.strftime('%y-%j', time.strptime(time.ctime())).split('-')]

def return_record_in_dataset(year, day):
    records = read_from_file(ds_path, get_lines=True)
    
    for i in range(len(records)):
        if i + 1 == len(records):
            return year, day, 0, -1
        i += 1
        record_year, record_day = records[i].split(',')[0].split('-')
        time_used = int(records[i].split(',')[1])
        
        if int(record_year) == year and int(record_day) == day:
            return int(record_year), int(record_day), time_used, i
    
    return year, day, 0, -1

if __name__ == '__main__':
    if not os.path.exists(ds_path.split('/')[0]):
        os.mkdir(ds_path.split('/')[0])
    
    if not check_file(ds_path):
        write_to_file(ds_path, 'Year_DayInYears, TimeUsedInSeconds\n')
    
    CounterThreat = threading.Thread(target=start_counting, args=(get_current_year_day(),), daemon=True)
    CounterThreat.start()
    
    try:
        print_per_percentage = float(input('enter print per percentage value[.2]: '))
    except BaseException:
        print_per_percentage = .2

    try:
        coldown_in_seconds = float(eval(input('enter time in seconds: ')))
    except BaseException:
        print('something went wrong...')
        exit()
    
    TimerThreat = threading.Thread(target=start_timer, args=(coldown_in_seconds, print_per_percentage))
    TimerThreat.start()
    