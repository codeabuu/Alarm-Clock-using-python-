#!/usr/bin/python3
import time
import datetime
import pytz


def set_alarm(time_set):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == time_set:
            print("Time to wake up and grind!")
            break
        else:
            print("Time is: " + current_time)
            time.sleep(1)
            snooze = input("Press any alphabet key to snooze: ")
            if snooze.isalpha():
                time_set = (datetime.datetime.now() + datetime.timedelta(minutes=1).strftime("%H:%M:%S"))
                print("Alarm snoozed for 1 min.")
            else:
                break
            time.sleep(1)

time_set = input("Enter time in HH:M:S: ")
set_alarm(time_set)
