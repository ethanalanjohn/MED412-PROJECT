from machine import Pin, PWM
import time
from light_sensor import read_light_intensity  # Import the function from light_sensor.py

# Define GPIO pins for motor control (using L298N motor driver)
IN1_PIN = 6
IN2_PIN = 7
ENA_PIN = 8  # PWM-capable pin for speed control

# Set up motor control pins
in1 = Pin(IN1_PIN, Pin.OUT)
in2 = Pin(IN2_PIN, Pin.OUT)
ena = PWM(Pin(ENA_PIN))  # Enable pin set as PWM for speed control
ena.freq(50)             # Set PWM frequency to 50 Hz

# Constants for rotation
FULL_ROTATION_DEGREES = 360
MAX_SPEED = 32768  # Adjust to control motor speed (0 to 65535 for PWM)

def motor_start():
    """ Start the motor to rotate in one direction """
    in1.high()
    in2.low()
    ena.duty_u16(MAX_SPEED)  # 50% duty cycle to control rotation speed

def motor_stop():
    """ Stops the motor """
    in1.low()
    in2.low()
    ena.duty_u16(0)  # Set PWM duty to 0 to stop the motor

def rotate_and_sample_light(rotation_duration=1.5, max_rotations=2):
    """
    Rotates the motor by 1 degree at a time and samples light intensity.
    Returns the maximum light intensity and the corresponding angle.
    """
    max_intensity = 0
    max_intensity_angle = 0
    angle_increment = 1  # Rotate 1 degree at a time
    total_angle = 0  # Track the total angle rotated

    for rotation in range(max_rotations):
        for angle in range(0, FULL_ROTATION_DEGREES, angle_increment):  # Rotate by 1 degree at a time
            motor_start()  # Start rotating the motor
            print(f"Rotating to angle {angle}°")
            time.sleep(rotation_duration / FULL_ROTATION_DEGREES)  # Adjust time per angle increment
            motor_stop()  # Stop motor briefly after each increment

            # Sample the light intensity here
            intensity = read_light_intensity()  # Call to your light sensor function
            print(f"Angle {angle}°: Light Intensity = {intensity}")  # Print intensity at each angle
            
            if intensity > max_intensity:
                max_intensity = intensity
                max_intensity_angle = angle

            total_angle += angle_increment
            if total_angle >= FULL_ROTATION_DEGREES:
                break  # Stop after one full rotation

    print(f"Maximum Light Intensity: {max_intensity} at angle {max_intensity_angle}°")
    return max_intensity, max_intensity_angle
