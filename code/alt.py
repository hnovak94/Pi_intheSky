import time
import board
import adafruit_mpl3115a2


i2c = board.I2C()  # uses board.SCL and board.SDA

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

# You can configure the pressure at sealevel to get better altitude estimates.
# This value has to be looked up from your local weather forecast or meteorological
# reports.  It will change day by day and even hour by hour with weather
# changes.  Remember altitude estimation from barometric pressure is not exact!
# Set this to a value in pascals:
sensor.sealevel_pressure = 99077
alt= []
while True:
	altitude = sensor.altitude
	alt.append(altitude) # add latest data to alt array
	print(alt) # bring array
	print(alt[0]) # print first altitude
	if altitude < alt[-3] # if current altitude is less than before
		print("apex") # will later be servos
	time.sleep(1.0)
	


