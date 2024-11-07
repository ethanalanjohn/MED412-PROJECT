from machine import Pin, PWM
import time

# Define GPIO pins
IN1_PIN = 2  # Change to your actual GPIO pins
IN2_PIN = 3
ENA_PIN = 0# PWM-capable pin for speed control

# Set up motor control pins
in1 = Pin(IN1_PIN, Pin.OUT)
in2 = Pin(IN2_PIN, Pin.OUT)
ena = PWM(Pin(ENA_PIN))  # Enable pin set as PWM for speed control
ena.freq(1000)  # Set PWM frequency for motor control

def motor_forward(speed):
    """ Spins the motor forward at the specified speed (0-1023). """
    in1.high()
    in2.low()
    ena.duty_u16(int(speed * 64))  # Convert speed to 16-bit value for duty cycle (0-65535)

def motor_backward(speed):
    """ Spins the motor backward at the specified speed (0-1023). """
    in1.low()
    in2.high()
    ena.duty_u16(int(speed * 64))

def motor_stop():
    """ Stops the motor by setting enable duty to 0. """
    ena.duty_u16(0)

# Example usage
try:
    while True:
        print("Motor Forward")
        motor_forward(1023)  # Set speed to half (0-1023 scale)
        time.sleep(2)       # Run forward for 2 seconds

        print("Motor Stop")
        motor_stop()
        time.sleep(1)       # Stop for 1 second

        print("Motor Backward")
        motor_backward(1023) # Run backward at half speed
        time.sleep(2)       # Run backward for 2 seconds

        print("Motor Stop")
        motor_stop()
        time.sleep(1)       # Stop for 1 second

except KeyboardInterrupt:
    motor_stop()
    print("Program stopped")
