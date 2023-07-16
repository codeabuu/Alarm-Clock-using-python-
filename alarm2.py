#!/usr/bin/python3
import time
import datetime


def set_alarm(time_set):
    while True:
        time_set = datetime.time()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time_left = (datetime.datetime.combine(datetime.date.today(), time_set) -
                     datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(current_time, "%H:%M:%S").time()))

        if current_time == time_set:
            print("Time to wake up and grind!")
            break
        else:
            print("Current time", current_time, end=" , ")
            print("Time left: ", time_left)
            time.sleep(1)
