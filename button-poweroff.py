# Derek Haas and Cameron Sullivan6-7-17
# Python script to power off Raspberry Pi using a button after payload retrieval

import RPi.GPIO as GPIO 
import time
from subprocess import call

GPIO.setmode(GPIO.BCM)
# Use GPIO pin 18 as input from the pushbutton.
GPIO.setup(18, GPIO.IN, pull_up_down= GPIO.PUD_UP)

while True:
	button= GPIO.input(18)
	# When the button is pressed, break the loop.
	if button == False: 
		print "button pressed"
		time.sleep(1)	
		break

# Shutdown the Pi when the button is pressed.
call(["sudo", "poweroff"])

			
