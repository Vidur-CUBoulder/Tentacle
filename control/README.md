Tentacle Control
===

Python program to run on the Raspberry pi. It accepts OSC messages of 4 values, and will then have the 4 stepper motors (A,B,C,D) try to move to those positions. "Position" is defined as steps away from the initial point where motors begin, either positive or negative. So an OSC messages of [1.0,-2.0,3.0,-4.0] will have stepper A move one step clockwise, stepper B move one step counter-clockwise, and so on.

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
