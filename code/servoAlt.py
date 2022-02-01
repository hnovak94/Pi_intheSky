import time
import board
import adafruit_mpl3115a2
from gpiozero import Servo

servo = Servo(18)

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
		if max(alt) - altitude > 1: # if current altitude is less than $
			print("apex") # will later be servos

			servo.max()
			time.sleep(0.5)
