from datetime import datetime

right_this_min = datetime.now().minute

if right_this_min % 2 == 0:
    print('This minute seems even')
else:
    print('This minute is odd')