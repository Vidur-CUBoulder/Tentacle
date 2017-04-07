#!/usr/bin/python
#
# Initial version: stan@wanderingstan.com
#

import Easydriver as ed
import time, threading
from math import copysign

class Stepper:
  """A class for controlling movement of stepper motor"""

  # Should stepper keep a thread running to continually update
  is_running = False

  debug = True

  # Current position of stepper (measured in steps away from zero point)
  current_position = 0.0
  goal_position = 0.0

  # Extema limits for this stepper
  max_position = +40.0
  min_position = -40.0

  update_interval_seconds = 0.01 # This might need to be controlled by higher class...

  # Pins on Pi
  pin_enable = 0
  pin_step = 0
  pin_dir = 0
  pin_ms1 = 0
  pin_ms2 = 0
  pin_ms3 = 0

  def __init__(self, pins_array, name="Stepper", update_interval_seconds=0.1):
    """Function to set all pins from array. Order is same as on Big Easy board"""
    self.pin_dir = pins_array.pop()
    self.pin_step = pins_array.pop()
    self.pin_sleep = pins_array.pop()
    self.pin_reset = pins_array.pop()
    self.pin_ms3 = pins_array.pop()
    self.pin_ms2 = pins_array.pop()
    self.pin_ms1 = pins_array.pop()
    self.pin_enable = pins_array.pop()
    self.name = name
    self.update_interval_seconds = update_interval_seconds

    """Create driver object with these pins for this stepper"""
    self.easydriver_stepper = ed.Easydriver(
      self.pin_step,
      self.update_interval_seconds/2, # Not sure how to handle this one...there are 2 timed parts to doing a step
      self.pin_dir,
      self.pin_ms1,
      self.pin_ms2,
      self.pin_ms3,
      self.pin_sleep,
      self.pin_enable,
      self.pin_reset,
      self.name
    )

  def set_zero_point(self):
    """Set the current stepper position as our zero point"""
    self.current_position = 0.0
    self.goal_position = 0.0

  def move_to_position(self, position_in_steps):
      """Set stepper to move to a given position"""

      if (position_in_steps > self.max_position) or (position_in_steps < self.min_position):
        print "Stepper position out of bounds, ignoring"
        return

      self.goal_position = position_in_steps
      if self.debug:
        print "%.4f-%s\tNEW goal position: %.2f" % (time.clock(), self.name, self.goal_position)

  def go(self):
    if not self.is_running:
      self.is_running = True
      self.update()

  def stop(self):
    self.is_running = False

  def update(self):
    """Move stepper towards goal."""

    # TODO: Later: Implement PID loop with encoders.

    if self.goal_position == self.current_position:
      # Do nothing if we're already there

      if self.debug:
        print "%.4f-%s\tIn goal position: %.2f" % (time.clock(), self.name, self.current_position)

    else:
      # Move toward goal
      goal_delta = self.goal_position - self.current_position

      # Determine direction
      direction = 1 if (goal_delta > 0.0) else 0 # 1/0 to indicate direction
      self.easydriver_stepper.set_direction(direction)

      # Make the move!
      # TODO: Implement ramp up and ramp down in movement speed
      move_steps = 1.0 # For now we always move one step.
      self.easydriver_stepper.step()

      # Record that we moved
      # TODO: This should come from encoders instead of this bookkeeping
      if direction == 1:
        self.current_position = self.current_position + move_steps
      else:
        self.current_position = self.current_position - move_steps

      if self.debug:
        print "%.4f-%s\tMoved: %.2f steps\tDirection: %s\tNew Position:%.2f" % (time.clock(), self.name, move_steps, direction, self.current_position)

    # If we're running, call this method again after time interval
    if self.is_running:
      threading.Timer(self.update_interval_seconds, self.update).start()




