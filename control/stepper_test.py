from Stepper import Stepper
import time

stepper_time_interval_seconds = 0.1
stepper_A = Stepper([1,2,3,4,5,6,7,8], "Stepper A", stepper_time_interval_seconds)
stepper_B = Stepper([1,2,3,4,5,6,7,8], "Stepper B", stepper_time_interval_seconds)
stepper_C = Stepper([1,2,3,4,5,6,7,8], "Stepper C", stepper_time_interval_seconds)
stepper_D = Stepper([1,2,3,4,5,6,7,8], "Stepper D", stepper_time_interval_seconds)


stepper_A.go()
stepper_B.go()
# stepper_C.go()
# stepper_D.go()

time.sleep(2)  # Sleep 5 seconds

stepper_A.move_to_position(32.0)
print ("Moved goal to 32")


time.sleep(4)  # Sleep 5 seconds

stepper_B.move_to_position(-26.0)
print ("Moved goal to 32")