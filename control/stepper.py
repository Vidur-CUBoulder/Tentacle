#!/usr/bin/python
#
# Initial version: stan@wanderingstan.com
#

import RPi.GPIO as GPIO

class stepper:
  """A class for controlling movement of stepper motor"""

  # Current position of stepper (measured in steps away from zero point)
  current_position = 0.0
  goal_position = 0.0

  # Extema limits for this stepper
  max_position = +4.0
  min_position = -4.0

  update_interval_seconds = 0.01 # THis might need to be controlled by higher class...

  # Pins on Pi
  pin_enable = 0
  pin_step = 0
  pin_dir = 0
  pin_ms1 = 0
  pin_ms2 = 0
  pin_ms3 = 0

  def set_zero_point():
    """Set the current stepper position as our zero point"""
    current_position = 0.0
    goal_position = 0.0


  def set_pins(pins_array):
    """Conenienve function to set all pins from array. Order is same as on Big Easy board"""
    pin_enable = pins_array[0]
    pin_ms1 = pins_array[1]
    pin_ms2 = pins_array[2]
    pin_ms3 = pins_array[3]
    pin_step = pins_array[4]
    pin_dir = pins_array[5]

    """Configure the pi to use these pins for this stepper"""

    # Enable Pin
    GPIO.setup(pin_enable, GPIO.OUT)
    GPIO.output(pin_enable, False)

    # Step Pin
    GPIO.setup(pin_step,GPIO.OUT)
    GPIO.output(pin_step, False)

    # Dir Pin: False=CCW, True=CW
    GPIO.setup(pin_dir,GPIO.OUT)
    GPIO.output(pin_dir, False)

    # Fine-tune pins
    GPIO.setup(pin_ms1, GPIO.OUT)
    GPIO.output(pin_ms1, False)

    GPIO.setup(pin_ms2, GPIO.OUT)
    GPIO.output(pin_ms2, True)

    GPIO.setup(pin_ms3, GPIO.OUT)
    GPIO.output(pin_ms3, False)

  def rotate_to(position):
      """Set stepper to move to a given position"""
      goal_position = position

  def update():
    """Move stepper towards goal"""
    GPIO.output(21, False)
    time.sleep(decel(count, maxCount))
    GPIO.output(21, True)




