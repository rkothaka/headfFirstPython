from datetime import datetime
import time
import random

odds = list(range(1, 60, 2))

for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd -", right_this_minute)
    else:
        print("Not an odd minute -", right_this_minute)

    wait_time = random.randint(1, 60)
    time.sleep(wait_time)
