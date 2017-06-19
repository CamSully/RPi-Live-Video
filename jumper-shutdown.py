# Derek Haas and Cameron Sullivan
# Script to shutdown Pi when jumper is removed
# June 19 2017

import RPi.GPIO as GPIO
import time
from subprocess import call

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
	jumperState = GPIO.input(21)
	time.sleep(2)
	if jumperState == True:
		print "jumper removed"
		time.sleep(3)
		break

call(["sudo", "poweroff"])
