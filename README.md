# Pi in the Sky

## Project Proposal

### Goal

Your task is to get your Pi into the sky. While in the sky, it should do two things:

Collect some data.

Make a sound or do something when it thinks it's at the apex of its flight.

### Project Idea

<b>Glitter Bomb</b>

The sphere will be launched into the air. When it reaches the apex of its flight, doors on the bottom will open via servos, and glitter will come out. A camera will take the picture as the glitter is released. 

### Problems

How will the doors close back up again?

How will the two halves of the sphere be attached?

### Code

[Readme](https://github.com/hnovak94/Pi_intheSky/blob/main/code/README.md)

#### Parts

- Raspberry Pi
- Altimeter (barometer) MPL3115A2; [starter code](https://github.com/adafruit/Adafruit_MPL3115A2_Library/blob/master/examples/testmpl3115a2/testmpl3115a2.ino)
- Pi Camera 
- 2 Servos SG92R; [library](https://gpiozero.readthedocs.io/en/stable/installing.html); [starter code](https://gpiozero.readthedocs.io/en/stable/api_output.html)

<b> What it does:</b> When the value read by the altimeter begins to drop the bottom half of the sphere opens (controlled by servos) and the camera will take a picture. 

The apex will be determined using an array. An itial value for the altimeter will become 'zero'. Every time the altimeter returns a value, the code will find the difference between the current value and the zero value. That difference will be added to the array. When the most recent array value is less than an older value in the array (maybe 5 values ago), then x will happen. 

The servos are going to move at the apex in order to open up the sphere [see CAD], the angle of which will have to be determined through trial and error--likely around 180 degrees. The camera will be fitted into a piece of acryllic in the center of the sphere. 

* Initial altimeter code: [alt.py](https://github.com/hnovak94/Pi_intheSky/blob/main/code/alt.py)
* Initial servo code: [servoAlt.py](https://github.com/hnovak94/Pi_intheSky/blob/main/code/servoAlt.py)
* Initial camera code: [altCam.py](https://github.com/hnovak94/Pi_intheSky/blob/main/code/altCam.py)


### CAD

#### Parts*

- Middle piece; circle of laser-cut acryllic
- Top half of the sphere; 3D printed
- Bottom half of the sphere; 3D printed, not identical to top half 
- 2 hinges; 3D printed, for the doors to open
- 2 doors; 3D printed, rounded, part of the bottom half
- Servo arms; 3D printed
- Glitter (not in CAD)

*Screws and nuts not included 

#### Initial Sketches and Design

<img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/gb_sketch.jpg" height="250"><img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/gb.capt.PNG" height="250">


