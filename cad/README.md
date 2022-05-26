# CAD

## Measurements

<b>Pi Camera:</b>

- holes: 18.85 x 10.39
- camera: 18.4 x 18.45
- 17.4 mm 
<img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/cammeasurements.png" height="250">
<b>Raspberry Pi:</b> 

- horizontal: edges of holes 55.5 mm apart
- vertical: edges of holes 20.2 mm apart 

<b>Altimeter:</b>

- holes: 11.41 mm apart 
- hole for wires: 4.56 mm x 18.9mm


### Prototype 1

<img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/p1.1.PNG" height="250"><img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/p1.2.PNG" height="250">

#### Problems:

The initial code was successful in opening the doors by turning 180 degrees, but the angle was slightly too large and it hit the edge of the ball. 
In order to fix this problem we switched the library from servo (which only has three settings, min(-90) mid(0) and max(90)) to AngularServo, where you can specify the angle of rotation. With this change to the code, the arm was unable to open the shell. 

The servo arm has three parts: the servo horn, an acryllic arm (bottom left), and an arm that is extruded from the shell door (bottom right). There are two possible points of movement: where the servo horn attaches to the arm, and where the arm attaches to the shell. We experimented with both. When we put the rotation point on the servo horn, the shell could fall open. When we put the rotation point on the shell arm, the shell could fall forwards. 

<img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/p1.3.PNG" height="100"><img src="https://github.com/hnovak94/Pi_intheSky/blob/main/media/p1.4.PNG" height="100">

We tried to glue the arm in place where the shell arm meets the hinge arm. We also had to screw the servo arm to the servo, because otherwise there was too much torque. 


