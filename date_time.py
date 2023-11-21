from datetime import datetime
from random import randint
from time import sleep

# iterate over the code 5 times
for i in range(5):
    right_this_min = datetime.now().minute
    if right_this_min % 2 == 0:
        print('This min seems even')
    else:
        print('This min seems odd')
    
    # sleep for random seconds
    seconds_to_sleep = randint(1,60)
    print('Sleeping for ', seconds_to_sleep, ' seconds')
    sleep(seconds_to_sleep)