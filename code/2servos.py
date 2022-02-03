# testing servo fix with two servos

from gpiozero import Servo
from time import sleep

myGPIO1 = 18 # servo one pin 18
myGPIO2 = 12 # servo two pin 12

# fixes servo range to be full 180 degrees
# tutorial: https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/
correction = 0.45
maxPW = (2.0 + correction)/1000
minPW = (1.0 - correction)/1000

servo1 = Servo(myGPIO1, min_pulse_width = minPW, max_pulse_width = maxPW)
servo2 = Servo(myGPIO2, min_pulse_width = minPW, max_pulse_width = maxPW)

while True:
  servo1.max() 
  servo2.max()
  # servos move 180 degrees
  sleep(0.5)
  servo1.min()
  servo2.min()
  # servos move -180 degrees
  sleep(0.5)
