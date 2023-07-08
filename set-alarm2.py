#!/usr/bin/python3
set_alarm = __import__('alarm2').set_alarm
set = set_alarm
enter_time = input("Enter time to wake up in HH:MM:SS respectively: ")
set(enter_time)
