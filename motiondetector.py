# Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
# [GCC 4.9.1] on linux

# Motion Detector
# Following tutorial called "Parent Detector" raspberrypi.org/learning
# Using Velleman VMA314 PIR (Passive IR) Motion Detector
#     RP1 adjusts time delay 0.3 sec to 18 sec
#     RP2 adjusts sensitivity 

from gpiozero import MotionSensor
from datetime import datetime
'''
# Initial demo 
pir = MotionSensor (4)
while True:
        if pir.motion_detected:
		print("Motion detected!")
'''

pir = MotionSensor (4)
while True:
        pir.wait_for_motion()
        print('{:%Y-%m-%d|%H:%M:%S}|1|MOTION'.format(datetime.now()))
        pir.wait_for_no_motion()
        print('{:%Y-%m-%d|%H:%M:%S}|0|IDLE'.format(datetime.now())) 
