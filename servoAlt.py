import time
import board
import adafruit_mpl3115a2
from gpiozero import Servo

servo = Servo(18)

i2c = board.I2C()

sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
num = 90
sensor.sealevel_pressure = 101000

while True: 

	altitude = sensor.altitude
	print(altitude)
	if altitude > num:
		servo.max()
		time.sleep(1)
		servo.mid()
		time.sleep(1)
		servo.min()
		time.sleep(1)
