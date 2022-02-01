import time
import board
import adafruit_mpl3115a2 # barometer library


i2c = board.I2C()  # uses board.SCL and board.SDA

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

# Set this to a value in pascals:
sensor.sealevel_pressure = 102574
# first = sensor.altitude
# print(first)
# time.sleep(1)
alt = [] # array for altitude values
lv = sensor.altitude
print(lv)
while True:
	print('')
	print(sensor.altitude) # initial value; zeroes it; 'launch value'
	print(sensor.altitude - lv)
