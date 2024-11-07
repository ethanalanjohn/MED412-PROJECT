# return_to_position.py
from motor_control import motor_start, motor_stop
import time

# Constants
FULL_ROTATION_DEGREES = 360

def return_to_max_intensity_position(max_intensity_angle):
    """
    Returns the motor to the position with the maximum light intensity.
    """
    print(f"Returning motor to max intensity position: {max_intensity_angle}°")
    # Rotate the motor to the max intensity angle
    target_time = (max_intensity_angle / FULL_ROTATION_DEGREES) * 1.5  # Adjust the time to rotate to the angle
    motor_start()
    time.sleep(target_time)  # Move motor to the calculated angle
    motor_stop()
    print("Motor returned to the max intensity position.")
