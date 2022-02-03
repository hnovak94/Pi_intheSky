import time
import board
import adafruit_mpl3115a2
from gpiozero import Servo

myGPIO1 = 18 # servo1 on pin 18
myGPIO2 = 12 # servo2 on pin 12


# fixes servo range to be full 180 degrees
# tutorial: https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/
correction = 0.45
maxPW = (2.0 + correction)/1000
minPW = (1.0 - correction)/1000

servo1 = Servo(myGPIO1, min_pulse_width = minPW, max_pulse_width = maxPW)
servo2 = Servo(myGPIO2, min_pulse_width = minPW, max_pulse_width = maxPW)

i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

sensor.sealevel_pressure = 102574
time.sleep(0.5)

alt = [] # array for altitude values
lv = sensor.altitude # initial value; zeroes it; 'launch value'

while True:
	altitude = sensor.altitude - lv
        # altitude is the diff between initial alt and current alt
	alt.append(altitude)
        # add latest data to alt array

	print(alt) # print array
	print(alt[0]) # print first altitude

	if len(alt) > 5: # if length of array is greater than 5
		if max(alt) - altitude > 1: 
		# if diff between max alt and current alt is greater than 1
			print("apex")

			servo1.max() # servos move 180 degrees
      servo2.max()
			time.sleep(0.5)
      
      with picamera.PiCamera() as camera:
        			camera.resolution = (1024, 768) # res
        			camera.start_preview()
        			sleep(1)
        			print("running")
        			camera.capture('../media/altcam.png')
        			print("done")
				sleep(1.0)
        
        servo1.min()
        servo2.min()
        time.sleep(0.5)
