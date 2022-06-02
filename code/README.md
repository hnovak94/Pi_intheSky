# Code

## Wiring

### Wiring Diagram

<img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/IMG-8581.jpg" height="250"> 

<img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/IMG-8584.jpg" height="300"><img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/IMG-8582.jpg" height="300"><img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/IMG-8583.jpg" height="300">

## Servos
* [gpiozero library](https://gpiozero.readthedocs.io/en/stable/installing.html)
* [Starter code](https://gpiozero.readthedocs.io/en/stable/api_output.html)

We temporarily tried using code where the angle input can be any angle between -90 and 90, rather than just using min, max, and mid. However, with this code the servo was not strong enough to open the shell. 

This [tutorial](https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/) helped fix the issue of the servo only moving 90 degrees. It offers a fix so the servo will complete the full range of motion. 

```
correction = 0.45
maxPW = (2.0 + correction)/1000
minPW = (1.0 - correction)/1000
    
```
Servo code would not work. Below shows troubleshooting process. When we attempted to open the [servoTest.py](https://github.com/hnovak94/Pi_intheSky/blob/main/code/servoTest.py) file, BeagleTerm would stop working, and we would have to close out and log back in. It is still unclear what the problem is, but it's possible the servos were dead. 

<img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/IMG-8529.jpg" height="350">

Replacing the servos did not seem to be the problem. As shown above, we checked the wiring and tried changing the pin number. 

## Altimeter
* [altimeter code](https://github.com/hnovak94/Pi_intheSky/blob/main/code/alt.py)

This code was fairly straightforward and ended up being the simplest part of the code. We used an array to store the altitude value. Because it was hard to get the air pressure to be exact, the altitude reading by the sensor was a little bit off. In order to try and "zero" the altitude, every value added to the array was not the raw number returned by the altimeter, but the value - initial value. The code above is commented to show the logic process. 

```
altitude = sensor.altitude - lv 

```
Below is the code for determining the apex of the flight:
```
if len(alt) > 5: # if length of array is greater than 5
		if max(alt) - altitude > 1: # if current altitude is less than before
			print("apex") # will later be servos
			time.sleep(0.5)
```
## Camera

The camera code was very simple, the important thing is to tell the pi where to save the picture. 
```
with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768) # res
        camera.start_preview()
        sleep(1)
        print("running")
        camera.capture('../media/altcam.png')
        print("done")
	sleep(1.0)
```
## Final Code
* [code](https://github.com/hnovak94/Pi_intheSky/blob/main/code/gb.py)

This code is basically just the altimeter code with the apex code filled in. Below shows what the code should do when the ball hits its apex.

```
# open doors
servo1.max() # servos move 180 degrees
servo2.max()
sleep(0.5)
			
# take picture 
 with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768) # res
        camera.start_preview()
        sleep(0.1)
        print("running")
        camera.capture('../media/bomb.png')
        print("done")
		sleep(1.0)
```
The problems with this are not clear. The problem did not seem to be with the code or with the wiring. The raspberry pi had trouble running the servos, often only one would work at a time. When I tried to run the code through BeagleTerm, it would often crash and I would have to start over. This was a major obstacle that set us back weeks. The servos would work individually with the servoTest.py code, but as soon as it had to deal with two servos it wouldn't work.

I got the battery to work with the pi, which made the two servos run at the same time. However, when I attempted to put the servos together with the altimeter the code overloaded the pi. 
