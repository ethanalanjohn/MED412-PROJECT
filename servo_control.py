from machine import Pin, PWM
import time

# Define the GPIO pin connected to the servo's signal pin
servo_pin = 15  # Update this to the correct GPIO pin for the servo

# Set up PWM for the servo motor
servo = PWM(Pin(servo_pin))
servo.freq(50)  # Standard frequency for servo motors (50 Hz)

# Function to set the servo position (0 to 90 degrees)
def set_servo_angle(angle):
    """ Set the servo motor to a specific angle. """
    min_duty = 1000  # Minimum duty cycle (0 degrees)
    max_duty = 9000  # Maximum duty cycle (90 degrees)

    # Map the angle (0-90) to the PWM duty cycle
    duty = int(min_duty + (angle / 90) * (max_duty - min_duty))
    servo.duty_u16(duty)

def launch_projectile():
    """ Rotate the arm from 0 to 90 degrees to launch the projectile, then reset slowly to the initial position. """
    print("Launching projectile...")

    # Set the servo to 0 degrees (starting position)
    set_servo_angle(0)
    time.sleep(1)  # Wait for the servo to reach the starting position

    # Rotate the arm to 90 degrees to launch the projectile
    set_servo_angle(180)
    time.sleep(1)  # Wait for the servo to reach the launching position
    
    # Slowly return the arm back to the initial position (0 degrees)
    for angle in range(180, -1, -2):  # Decrease angle from 90 to 0 in steps of 5
        set_servo_angle(angle)
        time.sleep(0.1)  # Adjust delay for smoother/slower motion

    print("Projectile launched and launcher reset to initial position!")

# Test the launch function
try:
    launch_projectile()

except KeyboardInterrupt:
    print("Program interrupted")
finally:
    servo.deinit()  # Clean up the servo control
