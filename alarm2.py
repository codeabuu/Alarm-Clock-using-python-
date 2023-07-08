#!/usr/bin/python3
import time
import datetime


def set_alarm(time_set):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == time_set:
            print("Time to wake up and grind!")
            break
        else:
            print(current_time)
            time.sleep(1)
