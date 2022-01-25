import time
import board
import adafruit_mpl3115a2


i2c = board.I2C()  # uses board.SCL and board.SDA

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

# Set this to a value in pascals:
sensor.sealevel_pressure = 99077

alt= []
lv = sensor.altitude # initial value; zeroes it

while True:
	altitude = lv - sensor.altitude 
	# altitude is the diff between initial alt and current alt
	alt.append(altitude)
	# add latest data to alt array

	print(alt) # print array
	print(alt[0]) # print first altitude

	if altitude < alt[-5] # if current altitude is less than before
	#	print("apex") # will later be servos
	time.sleep(1.0)
	


