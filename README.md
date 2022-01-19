# Pi in the Sky

## Project Proposal

### Goal

Your task is to get your Pi into the sky. While in the sky, it should do two things:

Collect some data.

Make a sound or do something when it thinks it's at the apex of its flight.


### Code

#### Parts

- Raspberry Pi
- Altimeter (barometer) MPL3115A2
- Pi Camera 
- 2 Continuous Servos; FS90R

<b> What it does:</b> When the value read by the altimeter begins to drop the camera will take a picture and the servos will move.

The apex will be determined using an array. Every time the altimeter returns a value it will be added to the array. When the current value is less than an older value in the array (maybe 5 values ago), then x will happen. 

The servos are going to move at the apex in order to open up the sphere [see CAD], the angle of which will have to be determined through trial and error. 


https://github.com/adafruit/Adafruit_MPL3115A2_Library/blob/master/examples/testmpl3115a2/testmpl3115a2.ino

### CAD

#### Parts*

- Middle piece; circle of laser-cut acryllic
- Top half of the sphere; 3D printed
- Bottom half of the sphere; 3D printed, not identical to top half 
- 2 hinges; 3D printed, for the doors to open
- 2 doors; 3D printed, rounded, part of the bottom half

*Screws and nuts not included 

#### Initial Sketches and Design


