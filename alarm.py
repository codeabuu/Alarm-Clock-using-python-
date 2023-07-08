#!/usr/bin/python3
import time
import datetime

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm_set(seconds):
    time_elapsed = 0


    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        hours_left = time_left // 3600
        minutes_left = time_left // 60
        second_left = time_left % 60

        print("{:02d}:{:02d}-{:02d}".format(hours_left, minutes_left, second_left))
