# Tentacle


## File Breakdown

1. Tenta\_wekproj \-  Wekinator project mapping incoming myo osc to x and y positional values. Data in data.arff
2. myo\-osc \- a myo to osc c++ library from https://github.com/samyk/myo-osc
3. sainsmart\_arm \- initial wekinator integration with mechanical arm for proof of concept
4. myo\_receiver.py \- Takes data from the myo\-osc program and outputs it to port 7777, then reroutes pertinent info to wekinator. 
5. stepper\_rpi.py \- Controls the stepper motor movement through rasp pi
6. tentacle\_arduino.ino \- Stepper control for arduino
