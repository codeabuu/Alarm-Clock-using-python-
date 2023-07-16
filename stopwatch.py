#!/usr/bin/python3
import time
import sys

def stopwatch():
    input("Press enter to start your count")
    start_time = time.time()
    print("stopwatch started")
    delay = 0.1

    while True:
        elap_t = (time.time() - start_time)

        minutes = int(elap_t // 60)
        seconds = int(elap_t % 60)
        milliseconds = int((elap_t % 1) * 1000)

        sys.stdout.write("\r")
        sys.stdout.write("Elapsed time is: {:02d} minutes, {:02d} seconds, {:02d} milliseconds".format(minutes, seconds, milliseconds))
        sys.stdout.flush()

        time.sleep(delay)

    print("\nStopwatch stopped!")

stopwatch()
