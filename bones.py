#!/usr/bin/env python3

import time
import argparse

def rest(rest_time):
    while rest_time:
        mins, secs = divmod(rest_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        rest_time -= 1
    print("End!")

def work(work_time):
    while work_time:
        mins, secs = divmod(work_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        work_time -= 1
    print("End!")

work_time = int(input("Enter seconds of work: "))
rest_time = int(input("Enter seconds of rest: "))

work(work_time)
rest(rest_time)
