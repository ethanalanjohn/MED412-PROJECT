# main.py
import time
from motor_control import rotate_and_sample_light
from return_to_position import return_to_max_intensity_position

# Constants for rotation and light intensity sampling
ROTATION_DURATION = 1.5  # Time for a full 360-degree rotation in seconds
MAX_ROTATIONS = 2  # Only rotate the motor 2 times

def main():
    try:
        # Rotate motor and sample light intensities, getting the maximum light intensity and angle
        max_intensity, max_intensity_angle = rotate_and_sample_light(rotation_duration=ROTATION_DURATION, max_rotations=MAX_ROTATIONS)
        
        # Print the max light intensity and the corresponding angle
        print(f"Maximum Light Intensity: {max_intensity} at angle {max_intensity_angle} degrees")

        # Return motor to the position with the maximum light intensity
        time.sleep(2)
        return_to_max_intensity_position(max_intensity_angle)

    except KeyboardInterrupt:
        print("Program interrupted.")

if __name__ == "__main__":
    main()
