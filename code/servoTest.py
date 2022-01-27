from gpiozero import Servo
from time import sleep

myGPIO = 18

# fixes servo range to be full 180 degrees
# tutorial: https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/
correction = 0.45
maxPW = (2.0 + correction)/1000
minPW = (1.0 - correction)/1000

servo = Servo(myGPIO, min_pulse_width = minPW, max_pulse_width = maxPW)

while True:
	servo.min() # -180 degrees
	sleep(1)
	servo.max() # 180 degrees
	sleep(1)
