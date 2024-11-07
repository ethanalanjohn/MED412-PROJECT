from machine import Pin
import time

# Define the GPIO pins
TRIG_PIN = 17  # GPIO Pin connected to TRIG of HC-SR04
ECHO_PIN = 16  # GPIO Pin connected to ECHO of HC-SR04

# Set up the TRIG pin as an output and the ECHO pin as an input
trigger = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

# Function to measure the distance
def measure_distance():
    # Send a pulse to the TRIG pin to start the ultrasonic burst
    trigger.high()
    time.sleep_us(10)  # Trigger pulse must last at least 10 microseconds
    trigger.low()

    # Measure the time it takes for the ECHO pin to go high and then low
    pulse_duration = time.pulse_us(echo, 1)  # Measure pulse duration in microseconds

    # The speed of sound is approximately 34300 cm/s, so we calculate the distance
    # Divide pulse_duration by 2 because it's the round trip (to the object and back)
    distance = (pulse_duration / 2) * 34300 / 1000000  # Convert to meters

    return distance

# Main loop
try:
    while True:
        # Get the distance and print it
        distance = measure_distance()
        print("Distance to target: {:.2f} meters".format(distance))
        time.sleep(1)  # Wait before the next measurement

except KeyboardInterrupt:
    print("Measurement stopped.")
