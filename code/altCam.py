from time import sleep
import board
import adafruit_mpl3115a2 # barometer library
import picamera # camera library


i2c = board.I2C()  # uses board.SCL and board.SDA

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

# Set this to a value in pascals:
sensor.sealevel_pressure = 99077

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
			with picamera.PiCamera() as camera:
        			camera.resolution = (1024, 768) # res
        			camera.start_preview()
        			sleep(1)
        			print("running")
        			camera.capture('../media/altcam.png')
        			print("done")
				sleep(1.0)
	
