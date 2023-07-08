#!/usr/bin/python3
from alarm import alarm_set
my_alarm = alarm_set
Hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
second = int(input("Enter number of secs: "))
total_mins = Hours * 60
total_seconds = total_mins * 60 + second
my_alarm(total_seconds)
