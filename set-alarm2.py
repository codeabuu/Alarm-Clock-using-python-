#!/usr/bin/python3
from alarm2.py import set_alarm
set = set_alarm
enter_time = input("Enter time to wake up in HH:MM:SS respectively: ")
set(enter_time)
