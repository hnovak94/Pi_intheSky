from gpiozero import Servo
from time import sleep

myGPIO = 18

# fixes servo range to be full 180 degrees
correction = 0.45
maxPW = (2.0 + correction)/1000
minPW = (1.0 - correction)/1000

servo = Servo(myGPIO, min_pulse_width = minPW, max_pulse_width = maxPW)

while True:
	servo.min()
	sleep(1)
	servo.max()
	sleep(1)
