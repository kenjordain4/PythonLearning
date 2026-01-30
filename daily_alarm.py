from plyer import notification
import time
from datetime import datetime,date
from format_time import format_input_time

def alarm(a,b):

    a=int(a)
    b=int(b)
    formatted_time=format_input_time(a,b)
    send_today=None
    while True:
        now=datetime.now()
        if now.hour==a and now.minute==b and send_today!=date.today():

            notification.notify(title="Alarm",message=f"It's{formatted_time},time to sleep",app_name="MyNotifier")
            send_today=date.today()
            print(f"Notification sent at {formatted_time}")
        #reset at midnight
        if now.hour==0 and now.minute==0:
            send_today=None


        time.sleep(60)
if __name__=="__main__":
    alarms=[(7,0),(22,0)]
    for a,b in alarms:
        alarm(a,b)

"""
Daily Alarm Notification App with Time Formatting Library

This Python program allows you to set one or more alarms that send desktop notifications
at specified times. The program is modular, using a custom library `format_time` to 
convert 24-hour input into human-readable 12-hour format with AM/PM.

Key Features:
- Supports multiple alarms stored in a list of (hour, minute) tuples.
- Uses `format_time` library to display alarm times in 12-hour AM/PM format.
- Sends desktop notifications using the `plyer` library.
- Each alarm is sent only once per day.
- Easy to extend with additional alarms or custom messages.

Library:
- `format_time.py` contains the function `format_input_time(hour, minute)` 
  which converts 24-hour times to 12-hour times with AM/PM.

Usage:
1. Import your library:
       from format_time import format_input_time
2. Set alarms:
       alarms = [(7, 0), (22, 0)]
3. Loop through the alarms and call the existing `alarm()` function:
       for a, b in alarms:
           alarm(a, b)
4. Run continuously to receive notifications.

Dependencies:
- Python 3.x
- plyer (install via `pip install plyer`)

Notes:
- Input times should be in 24-hour format (e.g., 22 for 10 PM).
- On Mac, make sure "Do Not Disturb" is off to see notifications.
- `format_time` library separates time formatting logic from alarm logic for modularity.
"""





