Tentacle Control
===

Python program to run on the Raspberry pi. It accepts OSC messages of 4 values, and will then have the 4 stepper motors (A,B,C,D) try to move to those positions. "Position" is defined as steps away from the initial point where motors begin, either positive or negative. So if steppers are currently at positions [10.0, 0.0, 6.0, 0.0], then an OSC messages of [1.0,-2.0,5.0,0.0] will have stepper A move 9 steps counter-clockwise, stepper B move two steps counter-clockwise, stepper C move 1 step clockwise, and stepper D does nothing.

Right now its hard coded that motors move only one step per update cycle.

Constants in the code can be modified to set how often the steppers update their position, OSC server address, and other settings.

To run:

    python TentacleControl.py

To test:
 - Run wekinator with 4 outputs.
 - Modify outputs to have range equal to steps of motion desired. (e.g. -40.0 to +40.0)
 - Move sliders

Note: `Stepper.py` will detect if you are *not* running on Raspberry Pi, and will use a stub file if not. This will show the same debug messages as real code, but (obviously) won't change do anything with GPIO.

