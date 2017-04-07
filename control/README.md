Tentacle Control
===

Python program to run on the Raspberry pi. It accepts OSC messages of 4 values, and will then have the 4 stepper motors (A,B,C,D) try to move to those positions. "Position" is defined as steps away from the initial point where motors begin, either positive or negative. So if steppers are currently at positions [10.0, 0.0, 5.0, 0.0], then an OSC messages of [1.0,-2.0,5.0,0.0] will have stepper A move 9 steps counter-clockwise, stepper B move two steps clockwise, and so on.

Right now its hard coded that motors move only one step per update cycle. 

Constants in the code can be modified to set how often the steppers update their position, OSC server address, and other settings. 

To run:

    python TentacleControl.py

To test:
 - Run wekinator with 4 outputs.
 - Move sliders

For developing locally, change line 6 of `Stepper.py`:

	import Easydriver_stub as ed

instead of:

	import Easydriver as ed
