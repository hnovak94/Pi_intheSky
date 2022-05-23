# Code


## Servos
* [gpiozero library](https://gpiozero.readthedocs.io/en/stable/installing.html)
* [Starter code](https://gpiozero.readthedocs.io/en/stable/api_output.html)

This [tutorial](https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/) helped fix the issue of the servo only moving 90 degrees. It offers a fix so the servo will complete the full range of motion. 

```
correction = 0.45
maxPW = (2.0 + correction)/1000
minPW = (1.0 - correction)/1000
    
```
Servo code would not work. Below shows troubleshooting process. When we attempted to open the [servoTest.py](https://github.com/hnovak94/Pi_intheSky/blob/main/code/servoTest.py) file, BeagleTerm would stop working, and we would have to close out and log back in. It is still unclear what the problem is, but it's possible the servos were dead. 

<img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/IMG-8529.jpg" height="250">

## Altimeter
