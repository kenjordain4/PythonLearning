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
