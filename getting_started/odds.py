from datetime import datetime

odds = list(range(1, 60, 2))
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd -", right_this_minute)
else:
    print("Not an odd minute -", right_this_minute)
