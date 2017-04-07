Tentacle Control
===

Python program to run on the Raspberry pi. It accepts OSC messages of 4 values, and will then have the 4 stepper motors (A,B,C,D) try to move to those positions. 

To run:

    python TentacleControl.py

To test:
 - Run wekinator with 4 outputs.
 - Move sliders

For developing locally, change line 6 of `Stepper.py`:

	import Easydriver_stub as ed

instead of:

	import Easydriver as ed
