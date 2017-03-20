#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

Step_pins = [26, 19, 13] #MS1, MS2, MS3

for pin in Step_pins:
  GPIO.setup(pin, GPIO.OUT)
  if pin == 19: # and pin == 26:
    GPIO.output(pin, True)
  else:
    GPIO.output(pin, False)

#ENABLE PIN
GPIO.setup(6,GPIO.OUT)
GPIO.output(6, False)

#STEP PIN
GPIO.setup(21,GPIO.OUT)
GPIO.output(21, False)

#DIR PIN False - CCW, True - CW
GPIO.setup(20,GPIO.OUT)
GPIO.output(20, False)

WaitTime = 0.01

def decel( count, maxcount):
  if count < maxcount/10 :
    countfrac = 10*(float(count)/maxcount)
    WaitTime = 0.01 + 0.09*(float(1-countfrac))
  elif count > 9*float(maxcount)/10:
    countfrac = (float(count)/maxcount) 
    #print countfrac
    WaitTime = 0.01 + 0.2*(countfrac-0.9)
    print WaitTime
  else:
    WaitTime = 0.01
    
  return WaitTime 
  

count = 0
maxCount = 200
while (count < maxCount):
  # make one step
  GPIO.output(21, False)
  time.sleep(decel(count, maxCount))
  GPIO.output(21, True)
  #time.sleep(WaitTime)
  count = count +1
  #print 'one step done and the count is:', count
print "Good Bye!"
GPIO.output(21, False)
#GPIO.output(6, True)
